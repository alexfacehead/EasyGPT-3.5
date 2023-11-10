from __future__ import annotations

# Import essentials
from openai import OpenAI

# Import helpers, constants and typing
from termcolor import colored
from typing import Optional
from typing import List
from src.utils.helpers import sum_content_length
from src.utils.logging import Logger
from src.utils.env_setup import EnvironmentSetup


log_obj = Logger()
logger = log_obj.get_logger()
env_and_flags = EnvironmentSetup()

class ChatCompletionGenerator:
    def __init__(self, temperature: Optional[float]=env_and_flags.temperature, prompt_num: Optional[int] = 0, openai_api_key: Optional[str] = env_and_flags.openai_api_key, model: Optional[str] = env_and_flags.model, super_charged: Optional[str] = env_and_flags.super_charged, top_p: Optional[float] = 0.5):
        """
        Constructor for the SystemMessageMaker class.

        Args:
            prompt_num (int, optional): The number of the prompt to use. Defaults to None.
            openai_api_key (str, optional): The API key for OpenAI. Defaults to None.
            model (str, optional): The model for OpenAI. Defaults to None.
            super_charged (str, optional): The super charged mode for GPT-4. Defaults to None.
        """
        self.client = OpenAI()
        self.prompt_num = prompt_num
        self.openai_api_key = env_and_flags.openai_api_key
        self.model = env_and_flags.model
        self.super_charged = env_and_flags.super_charged
        self.client.openai_api_key = self.openai_api_key
        self.temperature = env_and_flags.temperature
        self.top_p = env_and_flags.top_p

    def generate_completion(self, model, messages: List[dict], temperature: Optional[float]=0.33, top_p: Optional[float]=0.1) -> str:
        logger.info(f"MODEL ACTUALLY BEING USED: {model}")
        """
        Generates a completion using OpenAI's ChatCompletion API.

        Args:
            messages (List[dict]): A list of messages to start the completion. Each message is a dictionary containing 'role' and 'content' keys.
            model (str, optional): The model to use for the completion. Defaults to "gpt-3.5-turbo".
            temperature (float, optional): The higher the number used, the more statistical variation / randomness. Between 0.1-0.5 is reocmmended for coding and facts.

        Returns:
            str: The content of the completion generated by the model.
        """
        print(colored("\nGenerating completion...\n", 'magenta'))
        print(colored(f"Current context length: {sum_content_length(messages)}\n", 'red'))

        response = self.client.chat.completions.create(
            model=model,
            messages = messages,
            max_tokens = 4096,
            temperature = temperature,
            top_p = top_p
        )
        print(colored("--Successfully completed last API call--\n", 'blue'))
        return response.choices[0].message.content