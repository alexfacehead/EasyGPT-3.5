import argparse
import os
from dotenv import load_dotenv


class EnvironmentSetup:
    _instance = None

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(
            description="Tree-of-thought prompting pipeline using mixture-of-experts to enhance LLM outputs."
        )
        parser.add_argument("--model", type=str, help="Default OpenAI model (query mode, file naming, etc.).")
        parser.add_argument("--pipeline_model", type=str, help="Model used for the pipeline steps (expensive).")
        parser.add_argument("--temperature", type=float, help="Sampling temperature (higher = more creative).")
        parser.add_argument("--top_p", type=float, help="Nucleus sampling probability.")
        parser.add_argument("--query_mode", action="store_true", help="Enable interactive follow-up questions.")
        parser.add_argument("--openai_api_key", type=str, help="OpenAI API key.")
        parser.add_argument("--prompt_dir", type=str, help="Directory to save prompt/answer histories.",
                            default="resources/prompts")
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
        args = self.parse_arguments()

        self.openai_api_key = args.openai_api_key or os.getenv("OPENAI_API_KEY")
        self.model = args.model or os.getenv("MODEL", "gpt-5.1-mini")
        self.pipeline_model = args.pipeline_model or os.getenv("PIPELINE_MODEL", "gpt-5.1")
        self.temperature = args.temperature if args.temperature is not None else float(os.getenv("TEMPERATURE", "0.33"))
        self.top_p = args.top_p if args.top_p is not None else float(os.getenv("TOP_P", "0.5"))
        self.query_mode = args.query_mode or (os.getenv("QUERY_MODE", "").lower() == "true")
        self.prompt_dir = args.prompt_dir

        self._initialized = True
