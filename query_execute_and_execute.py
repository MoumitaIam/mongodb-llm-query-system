import json
from pymongo import MongoClient
import csv

# Import your query generator function here
# For example, if your file is query_generator.py and function is generate_mongo_query:
from query_generator import generate_mongo_query

def execute_query_and_export(natural_language_query):
    # Connect to MongoDB (update your connection string as needed)
    client = MongoClient("mongodb://localhost:27017/")
    db = client['your_database_name']
    collection = db['your_collection_name']

    # Generate MongoDB query filter dict from NL query
    mongo_query = generate_mongo_query(natural_language_query)

    # If the query generator returns string, parse it
    if isinstance(mongo_query, str):
        mongo_query = mongo_query.strip("` \n")
        mongo_query = json.loads(mongo_query)

    print("Generated MongoDB query filter:")
    print(json.dumps(mongo_query, indent=2))

    # Execute the query
    results = list(collection.find(mongo_query))

    print(f"\nNumber of documents found: {len(results)}")

    # Optionally, print some results (first 5)
    for doc in results[:5]:
        print(doc)

    # Export to CSV (optional)
    if results:
        keys = set()
        for doc in results:
            keys.update(doc.keys())
        keys = list(keys)

        with open('query_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for doc in results:
                writer.writerow(doc)

        print("\nResults exported to 'query_results.csv'")

if __name__ == "__main__":
    user_input = input("Enter your natural language query: ")
    execute_query_and_export(user_input)
