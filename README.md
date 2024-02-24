# PseudoGenius AI 🚀

Hey there! Welcome to **PseudoGenius AI**: Your new best friend for coding your own pseudocode language and converting it into runnable code in whatever language you need without worrying about syntax!

It supports both ChatGPT-4 and Gemini Pro!

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
Before you start turning pseudocode into real code, you need to enter your OpenAI API key to PseudoGenius AI. 

1. In your project directory, create a file named .env.
2. Open .env and add the following line:
```makefile

OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```
3. Replace your_openai_api_key with your actual OpenAI API key.
4. Replace your_gemini_api_key with your GEMINI API key from here.

You can get Google GEMINI API Key for free [here!](https://aistudio.google.com/app/apikey)

### Usage

1. Create your pseudocode code inside of pseudo.yaml file
2. Run the following command:

```bash

python main.py <engine> <language>
```

3. Replace engine with either "chatgpt" or "gemini" depending on the AI you want to use. 
4. Replace <language> with the programming language that you want. Hit enter, and watch the magic happen!

## Examples

Explore our [examples folder](examples/) to witness it in action and get inspired!

- [Http Server Pseudocode](/examples/httpServer/pseudo.yaml)
- [Returns random cat fact pseudocode](/examples/catFactFetcher/pseudo.yaml)

## Contributing

Feel free to fork the repo, make your changes, and hit us up with a pull request.

# License

Use it, modify it, and spread the love. Just remember to shout back here if you do something cool with it!

