from pymongo import MongoClient
from seedmerCreation import create_seedmer
from seedmer import seedmer
from operationKmer import create_unique_sequences

class NoSql:
    def __init__(self, mongodb_uri):
        self.mongodb_uri = mongodb_uri

    def connect_to_database(self, database_name):
        client = MongoClient(self.mongodb_uri)
        return client[database_name]

    def create_seedmer(self, filenames, k):
        for filename in filenames:
            create_seedmer(filename, k)

    def create_unique_sequences(self, filenames, k):
        for filename in filenames:
            create_unique_sequences(filename, k, seedmer)

    def uniqueSequence(self, taxid, k):
        db = self.connect_to_database('refseq')

        # Create seedmer for target filenames
        target_filenames = db['genomic'].find({'taxid': taxid}, {'filename': 1})
        self.create_seedmer(target_filenames, k)

        # Create unique sequences for non-target filenames
        non_target_filenames = db['genomic'].find({'taxid': {'$ne': taxid}}, {'filename': 1})
        self.create_unique_sequences(non_target_filenames, k)

        print("Unique k-mers in seedmer:", seedmer)


# Example usage
if __name__ == "__main__":
    mongodb_uri = 'mongodb://localhost:27017/'
    taxid = 83332
    k = 100

    sequences = NoSql(mongodb_uri)
    sequences.uniqueSequence(taxid, k)
