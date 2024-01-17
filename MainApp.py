from LLMProcessor import LLMProcessor
from JiraConnector import JiraConnector
import constants as C

class MainApp:
    def __init__(self, api_key):
        """
        Initialize MainApp with the API key for LLMProcessor.
        :param api_key: API key for LLMProcessor.
        """

        self.llm_processor = LLMProcessor(api_key)

    def run(self):
        """
        Main application flow. Gets task title, decides Jira usage, and handles task processing.
        """
        user_task_title = self.get_task_title()
        jira_use = self.get_jira_use()
        
        expnaded_task_scope = self.llm_processor.generate_task_description_from_title(user_task_title)

        self.display_output(user_task_title, expnaded_task_scope)

        if jira_use:
            jira_client = JiraConnector(C.JIRA_SERVER, (C.JIRA_ID, C.JIRA_API_TOKEN))
            jira_client.create_issue(C.JIRA_PROJECTID, user_task_title, expnaded_task_scope)

    def get_task_title(self):
        """
        Prompts the user for the task title.
        :return: Task title input by the user.
        """

        return input("Enter the title of the task you want a completed scope for: ")
    
    def get_jira_use(self):
        """
        Asks the user if they want to use Jira integration.
        :return: Boolean indicating user's choice for Jira integration.
        """

        while True:
            user_input = input("Do you want to generate the task in Jira (y/n)? Make sure you specified JIRA variables correctly in constants if y. ").strip().lower()
            if user_input in ['y', 'n']:
                return user_input == 'y'
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

    
    def display_output(self, title, description):
        """
        Displays the generated task description.
        :param title: Title of the task.
        :param description: Generated description of the task.
        """

        print (f"\nGenerated Task Description for {title}\n")
        print(description)

if __name__ == "__main__":
    
    app = MainApp(C.OPEN_AI_KEY)
    app.run()