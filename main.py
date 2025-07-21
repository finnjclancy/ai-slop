import os
from dotenv import load_dotenv

from api import get_completion

load_dotenv()

def get_memory():
    """
    Gets the agent's memory.
    """
    if os.path.exists("memory.txt"):
        with open("memory.txt", "r") as f:
            return f.read()
    else:
        return ""

def save_memory(memory):
    """
    Saves the agent's memory.
    """
    with open("memory.txt", "w") as f:
        f.write(memory)

def main():
    """
    Main function for the AI agent.
    """
    # Get the agent's memory
    memory = get_memory()

    # Get the current state of the repository
    repo_state = os.listdir(".")

    # Create the prompt
    prompt = f"""
    You are a self-improving AI agent.

    Your current memory is:
    {memory}

    The current state of the repository is:
    {repo_state}

    What do you want to do next?
    """

    # Get the agent's response
    response = get_completion(prompt)

    # Save the agent's response to memory
    save_memory(response)

    # Execute the agent's response
    exec(response)

if __name__ == "__main__":
    main()
