import sys
import yaml
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY", "")

def generate_code_with_gpt(pseudocode, language):
    # prompt for GPT-4, specifying the target programming language
    prompt = f"Convert the pseudocode below to {language} programming language code:
      - make sure that the code is complete with easy to run
      - test the code is executable
      - add comments to the code to make it easy to ready
      - return the code only with no description)
      
      pseudocode:\n{pseudocode}"
        
    # get the response from chatgpt 4 model
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

    # grab code only if there's description
    if "```" in result:
        result = result.split("```")[1]
        result = "\n".join(result.split("\n")[1:])

    return result