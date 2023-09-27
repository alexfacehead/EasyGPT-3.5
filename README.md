# System Message Maker (With Tree-of-Thought for Vastly Improved Quality With Only gpt-3.5-turbo)

## **With just a SINGLE sentence**, this script generates a highly optimized System Message for LLMs using OpenAI's GPT-3 model. 

It is cheap, requires running a single command, and has interactivity features, logging, and more.

By employing iterative prompting techniques and tree-of-thought, gpt-3.5-turbo model - which is incredibly cheap to use - produces surprisingly high quality System Messages which can then be used for more powerful models, like gpt-4 or gpt-3.5-turbo-16k.

The results are startling: just one sentence can result in - while slower responses - much cheaper, and equally powerful results as compared to ChatGPT 4, GPT-4-0314, GPT-4 and other state-of-the-art LLMs.

This has been tested with about a sample size of 20, and I'd love to hear feedback!


## Usage on Ubuntu or WSL

0. Setup a venv!

1. Run `pip install -r requirements.txt`

2. Execute `export OPENAI_API_KEY=your_actual_key_here` in a session (or set the value of `OPENAI_API_KEY` in the `.env.template` file and rename it to `.env`)

3. Run the script without any arguments to generate a new system message:

`python system-msg-maker.py`

## Usage on macOS

1. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` if you have both Python 2 and Python 3 installed.

2. Execute `export OPENAI_API_KEY=your_actual_key_here` in a terminal session (or set the value of `OPENAI_API_KEY` in the `.env.template` file and rename it to `.env`)

3. Run the script without any arguments to generate a new system message:

`python system-msg-maker.py` or `python3 system-msg-maker.py` if you have both Python 2 and Python 3 installed.

This will prompt you for user input for context generation, then it will generate and print the final system message. The final system message will be saved to a text file in the /prompts/ directory in the script's directory. The text files are named prompt_N.txt, where N is a number that increments with each run of the script.


# TO DO
- Better input validation
- More expansive options
- Integration into langchain
- Portability and overall design integration
- Internet connectivity coming soon
- Further optimizations and selective GPT-4 usage options coming soon
- Binary Search Tree encoding and vectorization to come soon (hosting issues!)
- More steerability and interactivity
- Rotational prompts coming soon
- Add queries/continuation
- Fine-tune usage of more powerful language models
- Fix flags
- Chat history! Free of training data theft
- Logging & advanced debug output (and suppression)

# RECENTLY ADDED
- Better documentation
- Super-charge option (for those with gpt-4 acccess)
- Removed clutter
- Added better instructions

(Please replace your_actual_key_here with your actual OpenAI API key.)
(This README.md was optimized with GPT-4)
