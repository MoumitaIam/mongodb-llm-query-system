# 🧠 Automated MongoDB Query System Using Offline LLM

This project enables natural language querying on a MongoDB database using an **offline LLM (Mistral 7B - GGUF)**. It converts user prompts into valid MongoDB queries, executes them, and returns results.

## 🚀 Features
- Load data from a CSV file into MongoDB
- Accept natural language queries
- Generate MongoDB filters using an offline model
- Execute queries and display/save results
- Log all generated queries

## 🛠️ Requirements
- Python 3.8+
- MongoDB (local)
- Python packages:
  - `pymongo`, `pandas`, `langchain`, `llama-cpp-python`

## ⚙️ Setup Instructions
```bash
# Clone the repo or copy the code locally

# Install required packages
pip install pymongo pandas langchain llama-cpp-python

# Place your CSV (e.g., sample_data.csv) in the project directory

# Run the script
python main.py
