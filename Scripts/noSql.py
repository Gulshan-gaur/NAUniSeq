from tqdm import tqdm
import progressbar
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

    def create_seedmer_SQl(self, filenames,count, k):
        target_progress = progressbar.ProgressBar(max_value=count)

        print('*********************************')        
        print("Creating Seedmer...")
        # Using tqdm to show progress for target filenames
        for i, filename in enumerate(filenames):
            create_seedmer(filename['filename'], k)
            target_progress.update(i + 1)

    def unique_sequences(self, filenames,count, k):
        print('*********************************')
        print("Creating unique sequences...")
        non_target_progress = progressbar.ProgressBar(max_value=count)
        for i,filename in enumerate(filenames):
            file = filename['filename']
            create_unique_sequences(file, k)
            non_target_progress.update(i+1)

    def uniqueSequence(self, taxid, k):
        db = self.connect_to_database('refseq')
        # Create seedmer for target filenames
        target_filenames = db['genomic'].find({'taxid': taxid}, {'filename': 1})
        if target_filenames:
            print('*********************************')        
            print("Database Connected")
        target_count = db['genomic'].count_documents({'taxid': taxid})    
        self.create_seedmer_SQl(target_filenames,target_count, k)
        print('*********************************')        
        print("Seedmer is craeted")
        # Create unique sequences for non-target filenames
        non_target_filenames = db['genomic'].find({'taxid': {'$ne': taxid}}, {'filename': 1})
        non_target_count = db['genomic'].count_documents({'taxid': {'$ne': taxid}})
        self.unique_sequences(non_target_filenames,non_target_count, k)
        print('*********************************')
        print("Unique k-mers in seedmer:", seedmer)
        print("Length of new seedmer",len(seedmer))

