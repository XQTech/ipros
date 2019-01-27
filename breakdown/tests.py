from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse
from breakdown.models import Ticket, Status, Customer
from breakdown.views import TicketList

# Create your tests here.
class TicketListPaginationTestCase(TestCase):
    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active">
        <a href="{}?page={}" class="page-link">{}</a>
    </li>
    """

    def setUp(self):
        Status.objects.create(
            code='test'
        )
        Customer.objects.create(
            name='test'
        )
        for n in range(15):
            Ticket.objects.create(
                status_id=1,
                customer_id=1,                
                ticket_no='TEST-01',
                description='Test Case',
                start_date='2019-01-10',
                end_date='2019-01-11',
                create_date='2019-01-10',
            )

    def testFirstPage(self):
        ticket_list_path = reverse('breakdown:TicketList')
        request = RequestFactory().get(path=ticket_list_path)
        response = TicketList.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(ticket_list_path, 1, 1),
            response.rendered_content)
