# System Message Maker (With Tree-of-Thought for Vastly Improved Quality With Only gpt-3.5-turbo)

## **With just a SINGLE sentence**, this script generates a highly optimized System Message for LLMs using OpenAI's GPT-3 model. 

It is cheap, requires running a single command, and has interactivity features, logging, and more.

By employing iterative prompting techniques and tree-of-thought, gpt-3.5-turbo model - which is incredibly cheap to use - produces surprisingly high quality System Messages which can then be used for more powerful models, like gpt-4 or gpt-3.5-turbo-16k. 


## Example Usage Images

1. First Usage
   ![First Usage](resources/example_usage_images/First%20Usage.png)

2. How to Input
   ![How to Input](resources/example_usage_images/How%20to%20input.png)

3. Final Output Example (Costs less than 0.01 USD)
   ![Final Output Example](resources/example_usage_images/Final%20Output%20Example%20(Costs%20less%20than%200.01%20USD).png)


## Usage on Ubuntu or WSL

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

## Extras

To use interactive mode, use the --query argument followed by your query:

`python3 system-msg-maker.py --query "Your query here"`

In interactive mode, the script will generate a response to your query using the latest system message saved in the /prompts/ directory. You can continue the conversation by entering new queries, and the conversation history will be updated and saved back to the file. Type exit to quit interactive mode.

You can also use the --num argument to specify a particular prompt file to use for the conversation:

`python3 system-msg-maker.py --query "Your query here" --num 2`

This will use the system message saved in prompt_2.txt for the conversation.

Finally, the --task argument can be used to modify the tree-of-thought component of the system message:

`python3 system-msg-maker.py --task`

When the --task argument is used, the tree-of-thought component will be changed to a task-oriented version. This argument can be combined with the --query and --num arguments.

Please replace `"Your query here"` with your actual query. Also, note that the paths in the commands are relative to the current working directory. Make sure to adjust them according to your actual file structure. This will be fixed soon.


# TO DO
- Better input validation
- More expansive options
- More steerability
- Integration into langchain
- Portability and overall design integration
- Internet access

# RECENTLY ADDED
- Better documentation
- Super-charge option (for those with gpt-4 acccess)
- Removed clutter
- Added better instructions

(Please replace your_actual_key_here with your actual OpenAI API key.)
(This README.md was optimized with GPT-4)
