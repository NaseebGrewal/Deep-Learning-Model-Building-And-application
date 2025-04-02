"""
This is a helper function to get the answer from OpenAI API.
It uses the OpenAI API to get the answer from the model.
file: __init__.py"""

from openai import OpenAI

# # Load the API key from the .env file
from dotenv import load_dotenv
load_dotenv()

def print_llm_response(prompt):
    """
    This function takes the response from the OpenAI API and prints the answer.
    :param response: The response from the OpenAI API
    """
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(completion.choices[0].message.content)
    return completion.choices[0].message.content