"""
This is a helper function to get the answer from OpenAI API.
It uses the OpenAI API to get the answer from the model.
file: __init__.py"""

import json
import os
from openai import OpenAI   

def get_api_key():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, 'config.json')

    with open(config_path) as config_file:
            config = json.load(config_file)
    api_key = config.get('api_key')

    return api_key


def print_llm_response(prompt):
    """
    This function takes the response from the OpenAI API and prints the answer.
    :param response: The response from the OpenAI API
    """

    api_key = get_api_key()
    client = OpenAI(api_key=api_key)

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


def get_llm_response(prompt):
    """
    This function takes the response from the OpenAI API and prints the answer.
    :param response: The response from the OpenAI API
    """

    api_key = get_api_key()
    client = OpenAI(api_key=api_key)

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


# print(get_llm_response("What is the capital of France?"))
# print(print_llm_response("What is the capital of France?"))





    # Process the response