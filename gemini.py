import json
import os

import google.generativeai as genai


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
genai.configure(api_key=GEMINI_API_KEY)
# specifying gemini-pro
model = genai.GenerativeModel('gemini-pro')


def generate_code_with_gemini(pseudocode, language):
    # the prompt for Gemini Pro
    prompt = (f"Task: Convert this pseudocode to executable {language} code. Focus on\n"
              "- Completeness: Ensure all necessary elements are translated to function as intended\n"
              "- Readability: Include comments for key logic explanations.\n"
              f"Pseudocode:\n{pseudocode}")

    # generating content for the Gemini Pro
    response = model.generate_content(prompt)
    
    # return the result
    result = response.text

    # get only the code 
    if "```" in result:
        result = result.split("```")[1]
        result = "\n".join(result.split("\n")[1:])

    return result
