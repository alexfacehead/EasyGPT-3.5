from typing import Optional
import os
import logging
from dotenv import load_dotenv

class Logger:
    _instance = None  # Singleton instance
    
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, log_dir: Optional[str] = "logs/", content: Optional[str] = ""):
        # This ensures that the initialization happens only once
        if not hasattr(self, 'initialized'):
            self.initialized = True
            load_dotenv('.env')

            # Set up logging
            os.makedirs(log_dir, exist_ok=True)
            log_file = os.path.join(log_dir, 'log.txt')
            logging.basicConfig(filename=log_file, 
                                level=logging.INFO, 
                                format='%(asctime)s %(levelname)s %(name)s %(message)s')
            self.logger = logging.getLogger(__name__)

            # Fetch environment variables
            self.OPENAI_API_KEY = self._get_env_variable('OPENAI_API_KEY')
            self.MODEL = self._get_env_variable('MODEL')
            self.SUPER_CHARGED = self._get_env_variable('SUPER_CHARGED')

            for key in ['OPENAI_API_KEY', 'MODEL', 'SUPER_CHARGED']:
                if not getattr(self, key):
                    self.logger.error(f"Please set the {key} either as an environment variable or in the .env file.")
                    exit(1)

            self.log_dir = log_dir
            self.prompt_dir = "resources/prompts/"

    def _get_env_variable(self, key: str) -> Optional[str]:
        value = os.getenv(key)
        if value:
            self.logger.info(f"{key} found. Value: {value}")
        else:
            self.logger.warning(f"{key} not found.")
        return value

    def get_dir(self) -> str:
        return self.log_dir
    
    def get_logger(self) -> logging.Logger:
        return self.logger
    
    def prompt_dir(self) -> str:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.logger.info(f"Script directory: {script_dir}")
        return os.path.join(script_dir, "../resources/prompts")
