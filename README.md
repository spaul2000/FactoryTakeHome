# FactoryTakeHome

# Project Setup Instructions

## Creating a New Conda Environment

To create a new Conda environment, follow these steps:

1. **Open your terminal**: Start your terminal application.

2. **Create a new Conda environment**: Run the following command, replacing `your_env_name` with the name you want to give to your environment.

   ```
   conda create -n your_env_name python=3.8
   ```

3. **Activate the new environment**: Once the environment is created, activate it using:

   ```
   conda activate your_env_name
   ```

## Installing Required Libraries

After creating and activating your Conda environment, install the required libraries listed in the `requirements.txt` file.


   ```
   pip install -r requirements.txt
   ```

   This command will install the libraries `langchain`, `openai`, and `jira`.

## Set Environment Constants for JIRA and OpenAI

Replace the following values in `constants.py` with your information:

```python
JIRA_SERVER = ''
JIRA_API_TOKEN = ''
JIRA_ID = ''
JIRA_PROJECTID = ''

OPEN_AI_KEY = ''
```

# Running the Main Application

After setting up your environment with the necessary configurations, you can start the application by running the following command in your terminal:

```
python MainApp.py
```

# LLM Configuration

## Customizing the Prompt
To adjust the prompt that the LLM uses, you can modify the string values in `prompts.py`. This allows for fine-tuning of the input provided to the language model. Providing a full example of a  ticket title and generation will improve response.

## Adjusting Model Parameters
For changes in the model's behavior, such as temperature settings or response token limits, you can make modifications in `LLMProcessor.py`. This provides control over the model's response characteristics and overall performance.