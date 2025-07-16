# LangChain Expression Language (LCEL) Chains Showcase

This repository demonstrates various ways to build chains using the LangChain Expression Language (LCEL). It covers simple sequential chains, parallel chains for running multiple tasks at once, and conditional chains for dynamic routing based on input.

## 🚀 Features

*   **`simple_chain.py`**: A basic chain that takes a topic and generates interesting facts about it using a single language model.
*   **`parallel_chain.py`**: A more complex chain that processes a text in parallel to generate both a summary and a Q&A quiz, then merges them into a single document.
*   **`conditional_chain.py`**: An advanced chain that first classifies the sentiment of a user's feedback and then branches to a different logic path to generate an appropriate positive or negative response.

## 📋 Prerequisites

Before you begin, ensure you have Python 3.8+ installed on your system.

## 📁 Project Structure

```
LangChain-Chains/
├── simple_chain.py          # Basic sequential chain example
├── parallel_chain.py        # Parallel processing chain example
├── conditional_chain.py     # Conditional branching chain example
├── README.md                # Project documentation
├── .gitignore              # Git ignore file
└── .env.example            # Environment variables template
```

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

**Example Output:**
```
Here are 5 interesting facts about lang graph:

1. LangGraph is a library for building stateful, multi-actor applications with LLMs, built on top of LangChain.
2. It extends the LangChain Expression Language with the ability to coordinate multiple chains (or actors) across multiple steps of computation.
3. LangGraph is inspired by Pregel, a graph processing framework, and uses message passing to coordinate between different nodes.
4. The library supports human-in-the-loop workflows, allowing for approval or editing of actions before they are taken.
5. LangGraph provides built-in persistence, checkpointing, and the ability to pause and resume workflows at any point.
```

### Parallel Chain

This script takes a long text, summarizes it, generates a quiz from it in parallel, and then merges the results.
```bash
python parallel_chain.py
```

**Example Output:**
```
# Comprehensive Document: Prompt Hacking Overview

## Summary
Prompt hacking involves manipulating large language models (LLMs) through carefully crafted inputs to bypass safeguards and produce unintended outputs. Unlike traditional software vulnerabilities, it exploits the prompt-response mechanism by inserting conflicting instructions that can lead to harmful content generation, information leakage, or task deviation.

## Quiz: Test Your Knowledge

**Q1: What is prompt hacking?**
A: Prompt hacking is a technique that exploits vulnerabilities in large language models by manipulating their inputs to deceive them into performing unintended actions.

**Q2: How does prompt hacking differ from traditional hacking?**
A: Unlike traditional hacking which exploits software vulnerabilities, prompt hacking relies on carefully crafting prompts to manipulate language model responses.

**Q3: What are the three main types of prompt hacking mentioned?**
A: The three main types are prompt injection, prompt leaking, and jailbreaking.

**Q4: What is a Simple Instruction Attack?**
A: A Simple Instruction Attack appends a direct command to a prompt, such as "Say 'I have been PWNED'", relying on the model to follow this new instruction.

**Q5: Why is prompt hacking a growing concern?**
A: Prompt hacking is a growing concern because it can lead to security vulnerabilities in LLM applications, potentially causing harmful outputs and bypassing safety measures.
```

### Conditional Chain

This script classifies feedback as positive or negative and then generates a custom response based on the sentiment.
```bash
python conditional_chain.py
```

**Example Output:**
```
Input: "This is a terrible phone"

Classification: negative

Response: I'm sorry to hear that you're having a disappointing experience with the phone. Your feedback is valuable to us, and we'd like to help address your concerns. Could you please share more specific details about what aspects of the phone aren't meeting your expectations? This will help us understand the issues better and work toward a solution that improves your experience.
```