from jira import JIRA
import constants as C

class JiraConnector:
    def __init__(self, jira_options, auth_tuple):
        """
        Initialize JiraConnector with JIRA options and authentication.
        :param jira_options: Dictionary containing JIRA server information.
        :param auth_tuple: Tuple for basic authentication (username, password/API token).
        """
        server = {
            'server': jira_options
        }
        self.jira = JIRA(options=server, basic_auth=auth_tuple)
    
    def create_issue(self, project_key, issue_title, summary):
        """
        Creates an issue in JIRA.
        :param project_key: The key of the JIRA project.
        :param issue_title: Title of the JIRA issue.
        :param summary: Summary or description of the issue.
        :return: Created issue object or None in case of failure.
        """
        try: 
            issue = self.jira.create_issue(
                fields={
                    "project": {"key": project_key},
                    "issuetype": {"name": "Task"},
                    "summary": issue_title,
                    "description": summary,
                }
            )
            return issue
        except Exception as e:
            print(f"An error occurred with uploading ticket to JIRA: {e}")
            
