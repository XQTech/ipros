from breakdown.models import Ticket, Breakdown, Status, FunctionGroup, Customer, BreakdownCategory
from breakdown import serializers as bds
from breakdown.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, viewsets, status
from django.http import Http404
from django.db.models import Q
from rest_framework.decorators import action, api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User
from .filters import TicketFilter
from jira import JIRA
from django.views import View
from django.conf import settings
import os
from docx import Document
from docx.shared import Inches
from openpyxl import Workbook
from openpyxl.styles import Fill, Border, Side, PatternFill, Alignment, Font, Color
from openpyxl.styles.colors import WHITE

DOC_PATH = settings.MEDIA_ROOT + 'breakdown/'

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tickets': reverse('ticket-list', request=request, format=format),
        'breakdowns': reverse('breakdown-list', request=request, format=format),
    })

class TicketViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Ticket.objects.all()
    serializer_class = bds.TicketSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = TicketFilter
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # def perform_create(self, serializer):
    #    serializer.save()


class BreakdownViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    
    queryset = Breakdown.objects.all()
    serializer_class = bds.BreakdownSerializer

    @action(detail=True)
    def breakdowns(self, request, pk=None):
        serializer = self.get_serializer(self.queryset.filter(ticket=pk), many=True)
        return Response(serializer.data)

class UploadImageView(APIView):
    def get_object(self, pk):
        try:
            return Breakdown.objects.get(pk=pk)
        except Breakdown.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):    
        bk = self.get_object(pk)
        print(self.request.FILES.get('file'))     
        if (bk.image1 == '' or bk.image1 == None):          
            bk.image1 = self.request.FILES.get('file')
        elif (bk.image2 == '' or bk.image2 == None):
            bk.image2 = self.request.FILES.get('file')
        elif (bk.image3 == '' or bk.image3 == None):
            bk.image3 = self.request.FILES.get('file')
        bk.save()
        bks = bds.BreakdownSerializer(bk)
        return Response(bks.data)
    
    def delete(self, request, pk, format=None):
        filename = self.request.query_params.get('name')
        bk = self.get_object(pk)
        if (bk.image1 != '' and bk.image1 != None and bk.image1.url.endswith(filename)):
            os.remove(settings.MEDIA_ROOT + bk.image1.url)
            bk.image1 = ''
        elif (bk.image2 != '' and bk.image2 != None and bk.image2.url.endswith(filename)):
            os.remove(settings.MEDIA_ROOT + bk.image2.url)
            bk.image2 = ''
        elif (bk.image3 != '' and bk.image3 != None and bk.image3.url.endswith(filename)):
            os.remove(settings.MEDIA_ROOT + bk.image3.url)
            bk.image3 = ''

        bk.save()
        return Response('{success:true}')


class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = bds.StatusSerializer

class FuncGroupsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FunctionGroup.objects.all()
    serializer_class = bds.FunctionGroupSerializer

class CustomersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = bds.CustomerSerializer

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = bds.UserSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BreakdownCategory.objects.all()
    serializer_class = bds.CategorySerializer

# For auth with JWT
class RestrictedView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        data = {
            'id': request.user.id,
            'username': request.user.username,
            'token': str(request.auth)
        }
        return Response(data)

class JiraView(APIView):

    queryset = None
    serializer_class = None
    def get(self, request, format=None):
        """
        Return a list of all issues.
        """
        jira_server = 'http://192.168.3.39:8080'
        jira_username = 'liqiang'
        jira_password = 'lq2017@gips'

        myjira = JIRA(jira_server,basic_auth=(jira_username,jira_password))
        # jql_str = "project%20%3D%20IPROS%20AND%20createdDate%20>%3D%202018-01-01%20AND%20type%20%3D%20Task%20"
        jql_str = "project = IPROS AND createdDate >= 2018-01-01 AND type = Task"
        fields = [
            'status',
            'fixVersions',
            'assignee',
            'key',
            'summary',
            'duedate',
            'customfield_10112',
            'id'
        ]
        data = myjira.search_issues(jql_str, 0, -1, True, fields, None, True)
        return Response(data)

class DocumentListView(APIView):
    queryset = None
    serializer_class = None

    def get(self, request, format=None):
        """
        Return a list of all docs.
        """
        data = []
        ticketFolders = os.listdir(DOC_PATH)
        print(ticketFolders)
        for folder in ticketFolders:
            fdPath = DOC_PATH + folder + '/'
            docName = 'FD-' + folder + '.docx'
            docs = []
            if os.path.exists(fdPath + docName):
                docs.append(docName)                
            
            xlsName = 'Breakdown-' + folder + '.xlsx'
            if os.path.exists(fdPath + xlsName):
                docs.append(xlsName)  

            data.append({
                    'ticket': folder,
                    'docs':docs
                })
        return Response(data)

class GenerateDocView(APIView):
    def get_ticket(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404
    
    def get_breakdown(self, pk):
        try:
            return Breakdown.objects.filter(ticket=pk)
        except Breakdown.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):    
        ticket = self.get_ticket(pk)
        breakdowns = self.get_breakdown(pk)
        docPath = DOC_PATH + ticket.ticket_no + '/'
        docName = docPath + 'FD-' + ticket.ticket_no + '.docx'
        xlsName = docPath + 'Breakdown-' + ticket.ticket_no + '.xlsx'
        self.generateDoc(ticket, breakdowns, docName, docPath)
        self.generateXls(ticket, breakdowns, xlsName, docPath)
        return Response(docName)

    def generateDoc(self, ticket, breakdowns, docName, docPath):
        document = Document()
        document.add_heading('FD - ' + ticket.ticket_no, 0)
        document.add_paragraph(ticket.summary)

        currentCategory = None
        currentFuncGroup = None
        for bk in breakdowns:
            category = bk.category
            funcGroup = bk.function_group
            if currentCategory == None or currentCategory != category.code:
                currentCategory = category.code
                document.add_heading(category.code, level=1)

            if currentFuncGroup == None or currentFuncGroup != funcGroup.description:
                currentFuncGroup = funcGroup.description
                document.add_heading(funcGroup.description, level=2)

            try:
                startIndex = bk.description.index('{')
                endIndex = bk.description.index('}') + 1
            except:
                startIndex = 0
                endIndex = 0
            if startIndex > 0 or endIndex > 0:
                document.add_paragraph(bk.description[endIndex:], style='List Bullet')
            else:
                document.add_paragraph(bk.description, style='List Bullet')
            if bk.image1 != '':
                document.add_picture(bk.image1, width=Inches(5.0))

            if bk.image2 != '':
                document.add_picture(bk.image2, width=Inches(5.0))

            if bk.image3 != '':
                document.add_picture(bk.image3, width=Inches(5.0))

        if os.path.exists(docName):
            os.remove(docName)
        if not os.path.isdir(docPath):
            os.mkdir(docPath)

        document.save(docName)
    
    def generateXls(self, ticket, breakdowns, docName, docPath):
        breakdowns = breakdowns.filter(effort__gt=0)
        wb = Workbook()
        ws = wb.active
        ws.title = 'Effort Breakdown'
        titleFont = Font(name='Arial', size=12, bold=True, color=WHITE)
        titleFill = PatternFill(patternType='solid', fill_type = 'solid', fgColor=Color('409EFF'))
        thin_border = Border(left=Side(style='thin'), 
                     right=Side(style='thin'), 
                     top=Side(style='thin'), 
                     bottom=Side(style='thin'))

        detailFont = Font(name='Arial', size=10, bold=False)
        startCol = 2
        startRow = 2
        ws.column_dimensions['A'].width = 2
        ws.column_dimensions['B'].width = 5
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 25
        ws.column_dimensions['E'].width = 80
        ws.column_dimensions['F'].width = 15
        self.createCell(ws, startRow, startCol, titleFont, titleFill, thin_border, 'SN')
        self.createCell(ws, startRow, startCol+1, titleFont, titleFill, thin_border, 'Category')
        self.createCell(ws, startRow, startCol+2, titleFont, titleFill, thin_border, 'Function Group')
        self.createCell(ws, startRow, startCol+3, titleFont, titleFill, thin_border, 'Items')
        self.createCell(ws, startRow, startCol+4, titleFont, titleFill, thin_border, 'Effort(mds)')

        currentCategory = None
        currentFuncGroup = None
        categoryStartRow = 0
        funcStartRow = 0
        i = 0
        row = startRow
        for bk in breakdowns:
            i = i + 1
            row = row + 1
            self.createCell(ws, row, startCol, detailFont, None, thin_border, i)
            category = bk.category
            funcGroup = bk.function_group

            self.createCell(ws, row, startCol+1, detailFont, None, thin_border, category.code)
            self.createCell(ws, row, startCol+2, detailFont, None, thin_border, funcGroup.description)
            try:
                startIndex = bk.description.index('{') + 1
                endIndex = bk.description.index('}')
            except:
                startIndex = 0
                endIndex = 0
            if startIndex > 0 or endIndex > 0:
                self.createCell(ws, row, startCol+3, detailFont, None, thin_border, bk.description[startIndex:endIndex])
            else:
                self.createCell(ws, row, startCol+3, detailFont, None, thin_border, bk.description)
            self.createCell(ws, row, startCol+4, detailFont, None, thin_border, bk.effort)
            
            if currentFuncGroup == None:
                funcStartRow = row
                currentFuncGroup = funcGroup.description
            elif currentFuncGroup != funcGroup.description:
                if funcStartRow < row - 1:
                    ws.merge_cells(start_row=funcStartRow, start_column=startCol+2, end_row=row - 1, end_column=startCol+2)
                funcStartRow = row
                currentFuncGroup = funcGroup.description

            if currentCategory == None:
                categoryStartRow = row
                currentCategory = category.code
            elif currentCategory != category.code:
                if categoryStartRow < row - 1:
                    ws.merge_cells(start_row=categoryStartRow, start_column=startCol+1, end_row=row - 1, end_column=startCol+1)
                categoryStartRow = row
                currentCategory = category.code
                # set index for func group
                if funcStartRow < row - 1:
                    ws.merge_cells(start_row=funcStartRow, start_column=startCol+2, end_row=row - 1, end_column=startCol+2)
                funcStartRow = row
                currentFuncGroup = funcGroup.description
            elif i == len(breakdowns) and categoryStartRow < row:
                ws.merge_cells(start_row=categoryStartRow, start_column=startCol+1, end_row=row, end_column=startCol+1)
                # set index for func group
                if funcStartRow < row:
                    ws.merge_cells(start_row=funcStartRow, start_column=startCol+2, end_row=row, end_column=startCol+2)

        formula = '=SUM(F' + str(startRow + 1) + ':F' + str(startRow + i) + ')'
        self.createCell(ws, startRow + 1 + i, startCol+4, titleFont, titleFill, None, formula)

        if os.path.exists(docName):
            os.remove(docName)
        if not os.path.isdir(docPath):
            os.mkdir(docPath)

        wb.save(docName)

    def createCell(self, ws, row, col, font=None, fill=None, border=None, value=''):
        col_sn = ws.cell(row=row, column=col, value=value)
        if font:
            col_sn.font = font
        if fill:
            col_sn.fill = fill
        if border:
            col_sn.border = border
        col_sn.alignment = Alignment(wrap_text=True)



