from jira import JIRA

jira_server = 'http://192.168.3.39:8080'
jira_username = 'liqiang'
jira_password = 'lq2017@gips'

myjira = JIRA(jira_server,basic_auth=(jira_username,jira_password))

print(myjira.user(myjira.current_user()))
for i in myjira.projects():
    print(i.name)