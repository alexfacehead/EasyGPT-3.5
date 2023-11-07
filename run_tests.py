import os
from dotenv import load_dotenv
from src.unit_testing.testing import test_temperature_runs

# Load the .env file into the environment
load_dotenv()

# Set defaults or get from environment
QUESTION= os.getenv('QUESTION')
TEMP_START_VALUE = float(os.getenv('TEMP_START_VALUE'))
TEMP_RANGE = int(os.getenv('TEMP_RANGE'))
SAVE_DIR = os.getenv('SAVE_DIR') if os.getenv('SAVE_DIR') is not None else str("src/unit_testing/unit_test_results")
REPEAT = int(os.getenv('REPEAT'))

def main():
    # Run the tests
    for i in range(REPEAT):
        test_temperature_runs(
            question=QUESTION,
            temp_start_value=TEMP_START_VALUE,
            temp_range=TEMP_RANGE,
            save_dir=SAVE_DIR,
            repeat=REPEAT
        )

if __name__ == '__main__':
    main()
