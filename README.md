# System Message Maker (With Tree-of-Thought for Vastly Improved Quality With Only gpt-3.5-turbo)

## **With just a SINGLE sentence**, this script generates a highly optimized System Message for LLMs using OpenAI's much weaker gpt-3.5-turbo-16k model, with high quality answers almost on par with ChatGPT 4.

It is **very** cheap, requires running a single command, and has interactivity features, logging, and more.

By employing iterative prompting techniques and tree-of-thought, gpt-3.5-turbo model - which is incredibly cheap to use - produces surprisingly high quality System Messages which can then be used for more powerful models, like gpt-4 or gpt-3.5-turbo-16k.

The results are startling: just one sentence can result in - while slower responses - much cheaper, and equally powerful results as compared to ChatGPT 4, GPT-4-0314, GPT-4 and other state-of-the-art LLMs.

This has been tested with about a sample size of 20, and I'd love to hear feedback!

## Use cases
- Generate a prompt or answer that can then be used with ChatGPT for excellent results, thereby saving money
- Extract content and ideas that only take one single sentence
- Save money but get quality results

## Usage on Ubuntu or WSL

0. Setup a venv. If you do not know how to do this, skip to the bottom.

1. Run `pip install -r requirements.txt`

2. Set the value of `OPENAI_API_KEY` in the `.env.template` file and rename it to `.env`
 - This will be fixed soon so that you may export or use flags.

3. Run the script without any arguments to generate a new system message:

`python EasyGPT-3.5.py` or `python3 EasyGPT-3.5.py` or whatever Python version you use.

4. You may also now set the temperature, running the same command as above, but with the flag `--temperature=0.5` for example. A temperature is a range from 0 to 2.
- `python3 main.py --temperature=0.1` may be useful for programming, for example, while creative writing may require a temperature from 0.3 to 1. The default is currently 0.33

## Usage on macOS

1. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` if you have both Python 2 and Python 3 installed.

2. Set the value of `OPENAI_API_KEY` in the `.env.template` file and rename it to `.env`

3. Run the script without any arguments to generate a new System Message, iteratively, slowly, but CHEAPLY, and receive an answer almost on-par with ChatGPT 4.

`python EasyGPT-3,5` or `python3 EasyGPT-3,5` if you have both Python 2 and Python 3 installed.

You may need to use python3, it depends on your speciifc setup.

**This will prompt you for user input for context generation**, then it will generate and print the final System Message **and answer**. The final system message will be printed, but not saved, to a directory. Work in progress.

Logging is soon to come, but the information and answers output are invaluable.

Simple fixes to this will be introduced soon.

# TO DO IN ORDER OF PRIORITY
- Update error handling (ex: no `--temperature-50.0` flag)
- Internet connectivity
- Fix flags and arguments, switch to pytest instead of unittest (high priority)
- More steerability and continuous querying
- Chat history! Free of training data theft
- Logging & advanced debug output (and suppression)
- Portability and overall design integration with other LLMs
- More expansive options: adaptable, automated hyperparameters based on context
- Binary Search Tree encoding and vectorization to come soon (hosting issues!)
- Integration with LangChain
- Rotational prompts (so as to reduce token overusage)
- Beautiful UI!
- Agentification (complex workflows)
- Reduce censorship (LOW PRIORITY)


# RECENTLY ADDED
- Streamlined, easy-to-use Unit Testing!! Usage is described in the **VENV** section right near bottom.
- Temperature flag! (`python3 main.py --temperature=0.5`` for example)
- Removeing clutter
- Added better instructions
- Experimenting with ultra-optimization
- Unit testing for tangible metrics (in-progress)
- Super-charge option [NOT WOKRING FOR NON-GPT-4 USERS]

(Please replace your_actual_key_here with your actual OpenAI API key in `.env.template` and rename it to `.env`.)

(This README.md was optimized with GPT-4)

# VENV
## Setting up `venv` for Python

### macOS & Linux

1. **Install Python** (if not already installed):
   - You can download from [Python's official website](https://www.python.org/downloads/).

2. **Install `venv`** (if not already included with your Python version):
   ```bash
   $ sudo apt-get install python3-venv  # For Ubuntu/Debian
   ```

3. **Create a virtual environment**:
   ```bash
   $ python3 -m venv myenv
   ```

4. **Activate the virtual environment**:
   ```bash
   $ source myenv/bin/activate
   ```

5. **Deactivate** (when done):
   ```bash
   $ deactivate
   ```

### Windows

1. **Install Python**:
   - Download from [Python's official website](https://www.python.org/downloads/).
   - Ensure Python and Pip are added to PATH during installation.

2. **Create a virtual environment**:
   ```bash
   C:> python -m venv myenv
   ```

3. **Activate the virtual environment**:
   ```bash
   C:\> myenv\Scripts\activate
   ```

4. **Deactivate** (when done):
   ```bash
   C:\> deactivate
   ```

*Note:* For projects requiring different Python versions or dependencies, repeat the steps to create a new virtual environment.

# Unit Testing (Contributions GREATLY welcomed - ALL confidential)

Use the `TestContentGenerator` for unit testing the performance of the `ContentGenerator` from the `src.content_creator` module.

### Overview
- Generate content based on various temperatures.
- Record timestamp, temperature, and elapsed time.
- Store results in a specified directory.

#### Flags Explanation
- `--question_test`: This specifies the question or prompt for the content generator test. Default is "What is the consensus on climate change?"
- `--temp_start_value`: This specifies which temperature value you'd like to start at. Default is 0.1. 
- `--temp_range`: Defines how many incremental temperature steps you'd like to test, starting from the `temp_start_value`. Default is 20.
- `--save_dir`: Directory where you want to save the test results. Default is "src/unit_testing/unit_test_results/".

#### Running the Test
From the root project directory, use:

```bash
python3 -m src.unit_testing.run_tests --question_test "What's 1+1?" --temp_start_value=0.1 --temp_range=10
```

`This README.md was optmized with GPT-4.`
