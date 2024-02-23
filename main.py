import sys
import yaml
import openai
import json
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")


# Language extension mapping
language_extensions = {
    'python': 'py',
    'javascript': 'js',
    'java': 'java',
    'c++': 'cpp',
    'c#': 'cs',
    'ruby': 'rb',
    'go': 'go',
    'rust': 'rs',
    'swift': 'swift',
    'kotlin': 'kt',
    'scala': 'scala',
    'php': 'php',
    'typescript': 'ts',
    'perl': 'pl',
    'lua': 'lua',
    'haskell': 'hs',
    'erlang': 'erl',
    'elixir': 'ex',
    'dart': 'dart',
    'clojure': 'clj',
    'groovy': 'groovy',
    'fortran': 'f90',
    'r': 'r',
    'matlab': 'm',
    'bash': 'sh',
    'powershell': 'ps1',
    'sql': 'sql',
    'html': 'html',
    'css': 'css',
    'xml': 'xml',
    'json': 'json'
}


def parse_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_code_with_gpt(pseudo_yaml, language):
    # Convert the YAML structure to a string that resembles pseudocode
    pseudocode = json.dumps(pseudo_yaml, indent=2)
    
    # Prepare the prompt for GPT-4, specifying the target programming language
    prompt = f"Convert the following pseudocode to {language} code ( make sure to give me comments and return the code only with no description):\n{pseudocode}"
    
    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.5,
        max_tokens=4096,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    result =  completion.choices[0].message.content
    if "```" in result:
        result = result.split("```")[1]
        result = "\n".join(result.split("\n")[1:])

    return result

def save_output(code, language):
    extension = language_extensions.get(language, 'txt')  # Fallback to .txt for unsupported languages
    filename = f"output.{extension}"
    with open(filename, 'w') as file:
        file.write(code)
    print(f"Code has been generated and saved to {filename}")

def main():
    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python main.py <language>")
        sys.exit(1)
    
    language = sys.argv[1].lower()
    yaml_path = "pseudo.yaml"

    if language not in language_extensions:
        print(f"Error: The specified language '{language}' is not supported.")
        sys.exit(1)
    
    pseudo_yaml = parse_yaml(yaml_path)
    code = generate_code_with_gpt(pseudo_yaml, language)
    save_output(code, language)

if __name__ == "__main__":
    main()