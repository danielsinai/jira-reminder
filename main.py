import os
from jira import JIRA
from slack_sdk import WebClient

jira_url = os.environ.get('JIRA_URL')
jira_username = os.environ.get('JIRA_USERNAME')
jira_api_token = os.environ.get('JIRA_API_TOKEN')
jql_query = os.environ.get('JQL_QUERY')

slack_token = os.environ.get('SLACK_TOKEN')
slack_channel_id = os.environ.get('SLACK_CHANNEL_ID')


jira = JIRA(server=jira_url, basic_auth=(jira_username, jira_api_token))

# Perform JQL query
issues = jira.search_issues(jql_query)

if issues:
    issue_info = ""
    for issue in issues:
        issue_info += f"- {issue.key}: {issue.fields.summary}\n"

    slack_client = WebClient(token=slack_token)

    slack_client.chat_postMessage(
        channel=slack_channel_id,
        text=f"Jira issues found:\n{issue_info}"
    )
    print("Slack notification sent!")
else:
    print("No Jira issues found.")
