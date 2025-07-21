# Self-Improving AI Agent

This project is an AI agent that can improve itself. It has access to a repository and an API key, and it uses these to update its own code and functionality.

## How it works

The agent's core logic is in the `main.py` file. This file contains the main loop that the agent runs, which includes the following steps:

1. **Observe:** The agent observes its environment, which includes the state of the repository and any new information from the user.
2. **Think:** The agent thinks about what it has observed and decides what to do next.
3. **Act:** The agent acts on its decision, which may include updating its own code, creating new files, or interacting with APIs.

The agent's memory is stored in the `memory` directory. This allows the agent to learn from its experiences and improve its performance over time.

## Getting started

To get started, you will need to create a `.env` file with your API key. You can then run the agent by running the following command:

```
python main.py
```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.
