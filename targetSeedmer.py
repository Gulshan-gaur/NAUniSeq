import gzip
from Bio import SeqIO

def seedmer(fileName,k):
    #Create kmer from a gzip fasta file
    global seedmer_dict
    reverse_records = []
    records = []
    with gzip.open(fileName, "rt") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            reverse = re.sub('[^GATC]', "", str(record.seq.reverse_complement()).upper())
            reverse_records.append(reverse)
            sequence = re.sub('[^GATC]', "", str(record.seq).upper())
            records.append(sequence)
        handle.close()
    all_records = records + reverse_records
    del records
    del reverse_records
    for dna in all_records:
        if len(dna)>=100:
            for i in range(len(dna)-k+1):
                val = dna[i:i+k]
                if val not in seedmer_dict:
                    seedmer_dict[val]=i
                del val
    del all_records
