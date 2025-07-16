# LangChain Expression Language (LCEL) Chains Showcase

This repository demonstrates various ways to build chains using the LangChain Expression Language (LCEL). It covers simple sequential chains, parallel chains for running multiple tasks at once, and conditional chains for dynamic routing based on input.

## 🚀 Features

*   **`simple_chain.py`**: A basic chain that takes a topic and generates interesting facts about it using a single language model.
*   **`parallel_chain.py`**: A more complex chain that processes a text in parallel to generate both a summary and a Q&A quiz, then merges them into a single document.
*   **`conditional_chain.py`**: An advanced chain that first classifies the sentiment of a user's feedback and then branches to a different logic path to generate an appropriate positive or negative response.

## 📋 Prerequisites

Before you begin, ensure you have Python 3.8+ installed on your system.

## ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd Chains
    ```

2.  **Create a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    This project uses `langchain`, `langchain-openai`, `langchain-google-genai`, `pydantic`, and `python-dotenv`. You can install them all with pip:
    ```bash
    pip install langchain langchain-openai langchain-google-genai pydantic python-dotenv
    ```

4.  **Set up your environment variables:**
    You will need API keys from OpenAI and Google to run these examples.

    *   Create a file named `.env` in the root of the project.
    *   Add your API keys to this file. **This file is included in `.gitignore` and will not be uploaded to GitHub.**

    Create a new file named `.env.example` to show what variables are needed.
    ```
    OPENAI_API_KEY="your_openai_api_key_here"
    GOOGLE_API_KEY="your_google_api_key_here"
    ```
    To run the code, copy `.env.example` to `.env` and fill in your actual keys.

## ⚡️ How to Run the Examples

Make sure you have followed the setup instructions and your virtual environment is active.

### Simple Chain

This script generates facts about a given topic.
```bash
python simple_chain.py
```

### Parallel Chain

This script takes a long text, summarizes it, generates a quiz from it in parallel, and then merges the results.
```bash
python parallel_chain.py
```

### Conditional Chain

This script classifies feedback as positive or negative and then generates a custom response based on the sentiment.
```bash
python conditional_chain.py
```