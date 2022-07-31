import gzip
from Bio import SeqIO

def operation_kmer(fileName,ftp_link):
    #Create kmer from a gzip fasta file
    global count
    reverse_records = []
    records = []
    with gzip.open('/mnt/drive/genomes/'+fileName, "rt") as handle:
        try:
            fasta_file = SeqIO.parse(handle, "fasta")
            for record in fasta_file:
                reverse = re.sub('[^GATC]', "", str(record.seq.reverse_complement()).upper())
                reverse_records.append(reverse)
                sequence = re.sub('[^GATC]', "", str(record.seq).upper())
                records.append(sequence)
            del fasta_file
            handle.close()
            all_records = records + reverse_records
            del records
            del reverse_records
            for dna in all_records:
                if len(dna)>=100:
                    for i in range(len(dna)-100+1):
                        val = dna[i:i+100]
                        if val in seedmer_dict:
                          del seedmer_dict[val]
                          count+=1
                        del val
            del all_records
        except Exception as e:
            with open('results/missing_.txt','a') as fw:
                fw.write(ftp_link)
                fw.write('\n')
                fw.close()
            print(str(e)+'hit missing')
