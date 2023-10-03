from dotenv import load_dotenv
from typing import Optional
import os
import logging
class Logger:
    _instance = None  # Singleton instance

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, log_dir: Optional[str] = "logs/"):
        # This ensures that the initialization happens only once
        if not hasattr(self, 'initialized'):
            self.initialized = True

            # Set up logging
            os.makedirs(log_dir, exist_ok=True)
            log_file = os.path.join(log_dir, 'log.txt')
            logging.basicConfig(filename=log_file, 
                                level=logging.INFO, 
                                format='%(asctime)s %(levelname)s %(name)s %(message)s')
            self.logger = logging.getLogger(__name__)
            self.log_dir = log_dir

    def get_logger(self) -> logging.Logger:
        return self.logger