from openai import OpenAI
import prompts as P

from langchain.llms import OpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

class LLMProcessor:
    def __init__(self, openai_api_key, temperature=0.5):
        """
        Initialize LangChain's LLM client with OpenAI's API key.
        :param openai_api_key: Your personal API key for OpenAI.
        :param temperature: Controls the randomness of the response.
        """
        self.llm = OpenAI(temperature=temperature, openai_api_key=openai_api_key)
    
    def generate_task_description_from_title(self, task_title):
        """
        Generates a detailed task description from a given title.
        :param task_title: Title of the task.
        :return: Detailed task description.
        """
        
        prompt = self.generate_prompt(task_title)
        response = self.prompt_langchain_llm(prompt)

        return response

    def generate_prompt(self, task_title):
        """
        Fills in message templates for prompt (modify system prompt in prompts if you desire different results)
        :param task_title: the title of the engineering task to give LLM.
        :return prompt: a ChatPromptTemplate instance representing the prompt.
        """
        system_prompt = SystemMessagePromptTemplate.from_template(
            P.inception_prompt)
        human_prompt = HumanMessagePromptTemplate.from_template(
            f"Expand the task title '{task_title}' into a detailed scope")

        prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
        return prompt.format()
    
    def prompt_langchain_llm(self, prompt, max_tokens=2048):
        """
        Sends a prompt to the LLM and retrieves the response.
        :param prompt: Prepared prompt for the LLM.
        :param max_tokens: Maximum length of the response.
        :return: LLM's response.
        """
        try:
            return self.llm(prompt, max_tokens=max_tokens)
        except Exception as e:
            breakpoint()
            print(f"An error occurred while communicating with the LLM: {e}")
            return None