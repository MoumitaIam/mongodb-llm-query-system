import pandas as pd
from pymongo import MongoClient

def load_csv_to_mongo(csv_file_path, mongo_uri, db_name, collection_name):
    # Read CSV file using pandas
    df = pd.read_csv(csv_file_path)

    # Convert 'Rating' and 'ReviewCount' columns to numeric types
    # Use errors='coerce' to convert invalid parsing to NaN, then fill NaNs with 0 or drop them
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce').fillna(0.0)
    df['ReviewCount'] = pd.to_numeric(df['ReviewCount'], errors='coerce').fillna(0).astype(int)

    # Convert DataFrame to dictionary records
    data = df.to_dict(orient='records')

    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Optional: Clear existing documents to avoid duplicates during testing
    collection.delete_many({})

    # Insert data into MongoDB collection
    collection.insert_many(data)
    print(f"Inserted {len(data)} records into {db_name}.{collection_name}")

if __name__ == "__main__":
    csv_file = "sample_data.csv"       # Your CSV filename here
    mongo_uri = "mongodb://localhost:27017"
    database_name = "testdb"           # Change if needed
    collection_name = "products"       # Change if needed

    load_csv_to_mongo(csv_file, mongo_uri, database_name, collection_name)

