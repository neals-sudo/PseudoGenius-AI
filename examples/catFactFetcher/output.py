import requests
import json

def GetRandomFact():
    # Send GET request
    print("Sending GET request...")
    response = requests.get("https://meowfacts.herokuapp.com/?count=1")

    # Make sure the http response is 200 and the response is valid
    if response.status_code != 200:
        print("Error occurred: HTTP response is not 200.")
        return None

    # Decode JSON response
    print("Decoding JSON response...")
    try:
        json_response = response.json()
    except json.JSONDecodeError:
        print("Error occurred: Unable to decode JSON response.")
        return None

    # Read Fact
    print("Reading fact...")
    try:
        fact = json_response['data'][0]
    except (KeyError, IndexError):
        print("Error occurred: Unable to read fact from JSON response.")
        return None

    # Return Fact
    print("Returning fact...")
    return fact

# Call the function
print(GetRandomFact())
