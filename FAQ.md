# Frequently Asked Questions (FAQ)

Welcome to the FAQ for the OpenAI ChatCompletions All-Model Enhancer. This document aims to address common questions and provide troubleshooting tips to help you set up and use the tool effectively across different operating systems.

## General Questions

### Q: What is the OpenAI ChatCompletions All-Model Enhancer?
A: It's a Python wrapper that simplifies generating prompts using OpenAI's ChatCompletions API. It's designed to enhance the quality of AI interactions and save all conversation history privately.

### Q: Which OpenAI models does this tool support?
A: The tool supports all models provided by OpenAI that are compatible with the ChatCompletions API, including the latest GPT-3.5 and GPT-4 models.

### Q: Is there a cost associated with using this tool?
A: The tool itself is free to use and open-source. However, using the OpenAI API may incur costs depending on your usage and the pricing plan you have with OpenAI. Starter accounts have $5 of free credit for models 3.5 and lower located at [https://platform.openai.com/playground](https://platform.openai.com/playground) where you can signup for free.

### Q: Can I use the more powerful models?
This depends on your OpenAI account and billing history. Making payments will increase your OpenAI tier and allow access to more models, higher queries per day, and higher tokens generated per minute.

## Installation and Setup

### Q: What are the system requirements for this tool?
A: You need Python 3.7 or higher and a virtual environment manager like `venv`. Internet access is also required to interact with the OpenAI API.

### Q: How do I set up the tool on macOS and Linux?
A: Follow these steps:
1. Open the Terminal.
2. Clone the repository using `git clone https://github.com/alexfacehead/EasyGPT-3.5`.
3. Navigate to the cloned directory with `cd EasyGPT-3.5`.
4. Create a virtual environment with `python3 -m venv env`.
5. Activate the virtual environment with `source env/bin/activate`.
6. Install dependencies with `pip install -r requirements.txt`.
7. Rename `.env.template` to `.env` and fill in your OpenAI API key and other settings.

### Q: How do I set up the tool on Windows?
A: Follow these steps:
1. Open Command Prompt or PowerShell.
2. Clone the repository using `git clone https://github.com/alexfacehead/EasyGPT-3.5`.
3. Navigate to the cloned directory with `cd EasyGPT-3.5`.
4. Create a virtual environment with `py -m venv env`.
5. Activate the virtual environment with `.\env\Scripts\activate`.
6. Install dependencies with `pip install -r requirements.txt`.
7. Rename `.env.template` to `.env` and fill in your OpenAI API key and other settings.

## Troubleshooting

### Q: What should I do if I encounter a `ModuleNotFoundError`?
A: Ensure that you have activated the virtual environment and installed all the required dependencies with `pip install -r requirements.txt`. If the problem persists, try deactivating (`deactivate`) and reactivating the virtual environment.

### Q: The program is not recognizing my OpenAI API key. What should I do?
A: Double-check that you have renamed `.env.template` to `.env` and correctly entered your API key without any typos. Ensure there are no extra spaces or characters in the `.env` file.

### Q: How can I resolve issues with the virtual environment on Windows?
A: Make sure you have the correct permissions to create and activate virtual environments. Run Command Prompt or PowerShell as an administrator if necessary. If you encounter errors related to `Scripts` not being in `PATH`, manually add the virtual environment's `Scripts` directory to your `PATH` or use the full path to activate the virtual environment.

### Q: The tool is running slowly or timing out. What can I do?
A: Check your internet connection to ensure it's stable and fast enough. If you're using a model like GPT-4, which requires more resources, consider switching to a smaller model for quicker responses. Also, review the OpenAI API status page for any ongoing issues, and check your rate limits on your OpenAI account.

### Q: How do I update the tool to the latest version?
A: Navigate to the tool's directory in your terminal or command prompt and run `git pull` to fetch the latest updates from the repository. Then, reinstall any updated dependencies with `pip install -r requirements.txt`.

### Q: Where can I find more information about the OpenAI API and its usage?
A: Visit the official OpenAI API documentation at [https://beta.openai.com/docs/](https://beta.openai.com/docs/) for comprehensive information on API capabilities, usage examples, and best practices.

### What about `git` and `venv`?

## Prerequisites Installation

Before you can use the OpenAI ChatCompletions All-Model Enhancer, you need to have `git` and a virtual environment manager like `venv` installed on your system. Here's how you can install these prerequisites on various operating systems:

### Installing `git`

#### Windows:
1. Download the latest Git for Windows installer from the [Git website](https://git-scm.com/download/win).
2. Run the installer and follow the prompts to complete the installation.
3. To verify the installation, open Command Prompt or PowerShell and type `git --version`.

#### macOS:
1. The easiest way to install Git on macOS is to use the standalone installer:
   - Download the latest macOS Git installer from the [Git website](https://git-scm.com/download/mac).
   - Follow the prompts to complete the installation.
2. Alternatively, you can use Homebrew, a package manager for macOS:
   - Install Homebrew by running `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` in the Terminal.
   - Once Homebrew is installed, run `brew install git`.
3. To verify the installation, open the Terminal and type `git --version`.

#### Linux:
1. Git is usually available in the official package repositories of most Linux distributions. Use your distribution's package manager to install it:
   - For Ubuntu/Debian-based systems, run `sudo apt-get install git`.
   - For Fedora, run `sudo dnf install git`.
   - For Arch Linux, run `sudo pacman -S git`.
2. To verify the installation, open the Terminal and type `git --version`.

### Installing `venv`

#### Windows:
1. `venv` is included by default with the Python installation from Python 3.3 onwards. Make sure you have Python installed:
   - Download the latest Python installer from the [Python website](https://www.python.org/downloads/windows/).
   - Run the installer, ensure you check the box that says "Add Python to PATH", and follow the prompts to complete the installation.
2. To verify the installation, open Command Prompt or PowerShell and type `python -m venv --help`.

#### macOS:
1. `venv` is included by default with Python. If you need to install Python:
   - You can download the latest Python installer from the [Python website](https://www.python.org/downloads/macos/).
   - Alternatively, if you have Homebrew installed, you can run `brew install python`.
2. To verify the installation, open the Terminal and type `python3 -m venv --help`.

#### Linux:
1. `venv` is typically included by default with Python in most Linux distributions. If you need to install Python:
   - For Ubuntu/Debian-based systems, run `sudo apt-get install python3-venv`.
   - For Fedora, run `sudo dnf install python3`.
   - For Arch Linux, Python is included by default.
2. To verify the installation, open the Terminal and type `python3 -m venv --help`.

## Additional Support

If your question isn't covered here or you need further assistance, please reach out to us at alexfacehead@hotmail.com with the subject line "EASYGPT SUPPORT", and we'll be happy to help.

