import gzip
from Bio import SeqIO
from .seedmer_data import seedmer

def create_seedmer(filename, k):
    with gzip.open(filename, "rt") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequence = str(record.seq)
            seq_len = len(sequence)
            
            # Sliding window technique
            for i in range(seq_len - k + 1):
                kmer = sequence[i: i + k]
                seedmer[kmer] = i
