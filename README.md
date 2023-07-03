# Jira Reminder

## Description

This is a side project to remind me of my Jira tasks that are still in any JQLable status.
Personally I use it to send me a daily Slack notification whenever there is a Bug assigned to me on Jira in "To Do" status with high priority.

Here is my JQL query:

```jql
project = PROJECTX AND assignee = \"daniel\" AND status = \"To Do\" AND sprint in openSprints() AND type = Bug AND priority = \"Now (Urgent)\""
```

## Deployment

1.  Create cronjob.prod.yaml 
    Use the template in the `cronjob.yaml` file to create a `cronjob.prod.yaml`
    replace those env variables with your own values in the cronjob.yaml:
    ```yaml
        env:
            - name: JIRA_URL
            value: "https://your-jira-url.com"
            - name: JIRA_USERNAME
            value: "username@example.com"
            - name: JIRA_API_TOKEN
            value: "your-api-token"
            - name: SLACK_TOKEN
            value: "your-slack-token"
            - name: SLACK_CHANNEL
            value: "your-slack-channel"
            - name: JQL_QUERY
            value: "project = YOUR_PROJECT AND status = \"To Do\""
    ```

2.  Apply the cronjob YAML definition

    ```bash
    kubectl apply -f cronjob.prod.yaml
    ```
3.  Test it via
    ```bash
    kubectl create job --from=cronjob/jira-reminder-cron test
    ```