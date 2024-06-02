import os
import pandas as pd
from pymongo import MongoClient

def insert_refseq_data(csv_file, mongodb_uri, db_name, collection_name):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Convert all numpy data types to native Python data types
    df = df.astype(object).where(pd.notnull(df), None)

    # Ensure all integer values are converted to standard Python int
    df['taxid'] = df['taxid'].apply(lambda x: int(x) if pd.notnull(x) else None)

    # Connect to the MongoDB server
    client = MongoClient(mongodb_uri)

    # Access the specified database and collection
    db = client[db_name]
    collection = db[collection_name]

    # Insert each row as a separate document in the MongoDB collection
    for _, row in df.iterrows():
        entry = {
            'taxid': row['taxid'],
            'filename': os.path.basename(row['link']),
            'assembly_level': row['assembly_level']
        }
        collection.insert_one(entry)

    print(f"Inserted {len(df)} records into {db_name}.{collection_name}")


if __name__ == "__main__":
    # Define the file path, MongoDB URI, database name, and collection name
    csv_file = 'test_data/refseq.csv' # Update this path if needed
    mongodb_uri = 'mongodb://localhost:27017/' # Update the URI if your MongoDB server is different
    db_name = 'refseq' # Replace with your database name
    collection_name = 'genomic' # Replace with your collection name

    # Insert data into MongoDB
    insert_refseq_data(csv_file, mongodb_uri, db_name, collection_name)
