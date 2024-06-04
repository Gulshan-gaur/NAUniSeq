import click
from pymongo import MongoClient
from .seedmerCreation import create_seedmer
from .seedmer_data import seedmer
from .operationKmer import create_unique_sequences

class NoSql:
    def __init__(self, mongodb_uri):
        self.mongodb_uri = mongodb_uri

    def connect_to_database(self, database_name):
        client = MongoClient(self.mongodb_uri)
        return client[database_name]

    def create_seedmer_SQl(self, filenames, k):
        for filename in filenames:
            create_seedmer(filename, k)

    def unique_sequences(self, filenames, k):
        for filename in filenames:
            print("processing the f{filename}")
            create_unique_sequences(filename, k, seedmer)

    def uniqueSequence(self, taxid, k):
        db = self.connect_to_database('refseq')
        print('*********************************')        
        print("Database Connected")
        # Create seedmer for target filenames
        target_filenames = db['genomic'].find({'taxid': taxid}, {'filename': 1})
        self.create_seedmer_SQl(target_filenames, k)
        print('*********************************')        
        print("Seedmer is craeted")
        # Create unique sequences for non-target filenames
        non_target_filenames = db['genomic'].find({'taxid': {'$ne': taxid}}, {'filename': 1})
        self.unique_sequences(non_target_filenames, k)

        print("Unique k-mers in seedmer:", seedmer)

