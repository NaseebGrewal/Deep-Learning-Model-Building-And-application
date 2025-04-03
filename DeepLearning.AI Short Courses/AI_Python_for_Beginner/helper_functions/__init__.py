"""
This is a helper function to get the answer from OpenAI API.
It uses the OpenAI API to get the answer from the model.
file: __init__.py"""

from openai import OpenAI
from dotenv import load_dotenv
from os import getenv
load_dotenv()        


def print_llm_response(prompt, API_KEY=getenv("API_KEY")):
    """
    This function takes the response from the OpenAI API and prints the answer.
    :param response: The response from the OpenAI API
    """

    # api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=API_KEY)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content

# API_KEY = getenv("API_KEY")
# print(API_KEY)