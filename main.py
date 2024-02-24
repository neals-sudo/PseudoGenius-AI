import sys
import yaml
import json
from chatgpt import generate_code_with_gpt
from gemini import generate_code_with_gemini


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


def save_output(code, language):
    extension = language_extensions.get(language, 'txt')  # Fallback to .txt for unsupported languages
    filename = f"output.{extension}"
    with open(filename, 'w') as file:
        file.write(code)
    print(f"Code has been generated and saved to {filename}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <engine> <language>")
        sys.exit(1)
    
    engine = sys.argv[1].lower()
    if engine not in ["chatgpt", "gemini"]:
        print(f"Error: The specified engine '{engine}' is not supported. Support engines: chatgpt, gemini")
        sys.exit(1)
    language = sys.argv[2].lower()
    if not language:
        print(f"Error: Language string is empty.")
        sys.exit(1)
    
    # Parse the YAML code
    yaml_path = "pseudo.yaml"
    pseudo_yaml = parse_yaml(yaml_path)

    # Convert the YAML structure to a string that resembles pseudocode
    pseudocode = json.dumps(pseudo_yaml, indent=2)

    # get the code generated
    if engine == "gemini":
        code = generate_code_with_gemini(pseudocode, language)
    else:
        code = generate_code_with_gpt(pseudocode, language)

    # save to output
    save_output(code, language)


if __name__ == "__main__":
    main()
