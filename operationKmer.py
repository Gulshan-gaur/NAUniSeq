import gzip,os
from Bio import SeqIO
from seedmer import seedmer

def create_unique_sequences(filename, k):
    file_path = '/mnt/drive/refesq/'
    with gzip.open(os.join_path(file_path,filename), 'rt') as f:
        for record in SeqIO.parse(f, 'fasta'):
            sequence = str(record.seq)
                # Sliding window technique
            for i in range(len(sequence) - k + 1):
                kmer = sequence[i:i+k]
                
                # Check if k-mer is present in seedmer
                if kmer in seedmer:
                    del seedmer[kmer]

