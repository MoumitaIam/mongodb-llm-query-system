# Automated MongoDB Query System Using Offline LLM

## Project Description
This Python project automates querying a MongoDB database using natural language input. It leverages an offline LLM (Mistral 7B) to generate MongoDB queries dynamically based on user prompts. The system supports:

- Loading CSV data into MongoDB.
- Generating MongoDB filter queries from natural language.
- Executing queries and displaying results.
- Saving results as CSV files.
- Logging generated queries for reference.

## Requirements
- Python 3.8 or higher
- MongoDB installed and running locally
- Python packages: `pymongo`, `pandas`, `langchain`, `llama-cpp-python`

## Setup Instructions
1. **Install MongoDB**  
   Download and install MongoDB Community Edition and start the service.

2. **Install Python dependencies**  
   ```bash
   pip install pymongo pandas langchain llama-cpp-python
3. **Download the model**
Download the mistral-7b.gguf model file and place it in the project directory.

4. **Prepare your CSV file**
Ensure your data CSV file (e.g., sample_data.csv) is in the project folder.

5. **Usage**
Run the main script:

bash
Copy
Edit
python main.py
When prompted, type your query in natural language (e.g.,
“Find products with Rating greater than 4.5”).

The system will generate and display the corresponding MongoDB query, run it, and show matching documents.

You can choose to save the query results to a CSV file.

To exit the program, type:

bash
Copy
Edit
exit


6. **Output Files**
query_results.csv: CSV file containing query results (if saved).

Queries_generated.txt: Log file containing all MongoDB queries generated during the session.
