import argparse
import os
from dotenv import load_dotenv

class EnvironmentSetup:
    _instance = None

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description="An easier and far cheaper way to use the gpt-3.5-turbo API, with results nearly comparable to ChatGPT 4 - with more additions coming soon!")
        parser.add_argument("--model", type=str, help="Your chosen OpenAI model")
        parser.add_argument("--temperature", type=float, help="Higher value is more random/creative.")
        parser.add_argument("--query_mode", type=bool, help="Enter True or False to continue asking questions in this context.")
        parser.add_argument("--openai_api_key", type=str, help="Your OPENAI_API_KEY")
        parser.add_argument("--super_charged", type=lambda x: (str(x).lower() == 'true'), help="If you have access to GPT-4, empowers results.")
        parser.add_argument("--prompt_dir", type=str, help="The directory for which you'd like to save your prompts and answer histories.", default="resources/prompts")
        return parser.parse_args()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EnvironmentSetup, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        load_dotenv()
        self.args = self.parse_arguments()
        self.openai_api_key = self.args.openai_api_key if self.args.openai_api_key is not None else os.getenv("OPENAI_API_KEY")
        self.model = self.args.model or os.getenv("MODEL")
        self.super_charged = self.args.super_charged if self.args.super_charged is not None else (os.getenv("SUPER_CHARGED") == 'True')
        self.temperature = self.args.temperature or None
        self.query_mode = self.args.query_mode or None
        self.prompt_dir = self.args.prompt_dir or None
        
        self._initialized = True
