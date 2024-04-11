from Bio.Blast import NCBIWWW, NCBIXML

def perform_blast(query_sequence, database="nt", evalue=0.001,qblast='nucleotide'):
    """
    Perform BLASTn search using Biopython.

    Parameters:
    - query_sequence (str): The sequence to be used as a query.
    - database (str): The BLAST database to search against (default is "nt").
    - evalue (float): The E-value threshold for the search (default is 0.001).

    Returns:
    - results (list): List of BLAST results.
    """
    try:
      if qblast=='nucleotide':
        # Perform BLASTn search
        result_handle = NCBIWWW.qblast("blastn", database, query_sequence, expect=evalue)
      else:
        result_handle = NCBIWWW.qblast("blastp", database, query_sequence, expect=evalue)
      # Parse the BLAST results
      blast_records = NCBIXML.read(result_handle)
      result_handle.close()

      return blast_records.alignments

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

for seq_name, seq in seedmer_dict.items():
    print(f"\nPerforming BLASTn search for {seq_name}...")
    blast_results = perform_blast(seq)

    # Display the top BLAST hit for each sequence
    if blast_results:
        top_hit = blast_results[0]
        print(f"Top BLAST hit for {seq_name}: {top_hit.title} (E-value: {top_hit.hsps[0].expect})")
    else:
        print(f"No BLAST hits found for {seq_name}")
