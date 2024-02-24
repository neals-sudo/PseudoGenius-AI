import json
import os

import google.generativeai as genai


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
genai.configure(api_key=GEMINI_API_KEY)
# specifying gemini-pro
model = genai.GenerativeModel('gemini-pro')


def generate_code_with_gemini(pseudocode, language):
    
    
    # the prompt for Gemini Pro
    prompt = f"Convert the pseudocode below to {language} programming language code:
      - make sure that the code is complete with easy to run
      - test the code is executable
      - add comments to the code to make it easy to ready
      - return the code only with no description)
      
      pseudocode:\n{pseudocode}"
    
    # generating content for the Gemini Pro
    response = model.generate_content(prompt)
    
    # return the result
    result =  response.text

    # get only the code 
    if "```" in result:
        result = result.split("```")[1]
        result = "\n".join(result.split("\n")[1:])

    return result