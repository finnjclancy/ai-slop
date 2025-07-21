import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt):
    """
    Gets a completion from the OpenAI API.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
