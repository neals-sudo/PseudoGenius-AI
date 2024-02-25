# PseudoGenius AI 🚀

The future of programming is here! Effortlessly transform pseudocode into real code across languages with the groundbreaking power of ChatGPT-4 and Gemini Pro.

## How it works

Design your pseudocode in any style you like, using the versatile YAML syntax. This solution effortlessly transforms it into code for your chosen programming language, eliminating the need to memorize syntax details.

## Getting Started

First things first, let's get you set up. You're going to need Python and some magic spells (aka libraries) to get rolling.

### Installation

After you clone the project, cd to the project's directory and run:

```bash
pip install -r requirements.txt
```

### Setting Up Your OpenAI Key
To use PseudoGenius AI, you'll need API keys for the AI models it supports.

1. Create a .env file: In the project's root directory, create a new file named .env. This will store your API keys securely.

2. Add your keys to .env:

```makefile
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```
- Replace your_openai_api_key with your actual OpenAI API Key (obtainable from your OpenAI account).
- Replace your_gemini_api_key with your Gemini API key. Follow the link below to get one.

Get Your Free Gemini API Key [here](https://aistudio.google.com/app/apikey)

### Usage
1. Craft your pseudocode in pseudo.yaml: Ensure your pseudocode is saved within the [pseudo.yaml](/pseudo.yaml) file.
2. Execute the main script: Run the following command in your terminal:

```bash
python main.py <engine> <language>
```
- Choose Your Engine: Replace <engine> with either chatgpt or gemini to select your desired AI model.
- Specify the Language: Replace <language> with the target programming language (e.g., python, javascript, java, etc.).


Absolutely! Here's a revised version of your README.md usage section, focusing on clarity, consistency, and a slightly more professional tone:

Usage
Craft your pseudocode in pseudo.yaml: Ensure your pseudocode follows the expected format and is saved within the pseudo.yaml file.

Execute the main script: Run the following command in your terminal:

### Example Usage:

To generate Python code using ChatGPT, you would run:

```bash
python main.py chatgpt python
```

## Examples

Explore our [examples folder](examples/) to witness it in action and get inspired!

- [Http Server Pseudocode](/examples/httpServer/pseudo.yaml)
- [Returns random cat fact pseudocode](/examples/catFactFetcher/pseudo.yaml)

## Contributing

Feel free to fork the repo, make your changes, and hit us up with a pull request.

# License

Use it, modify it, and spread the love. Just remember to shout back here if you do something cool with it!

