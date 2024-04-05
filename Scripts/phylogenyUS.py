import click
import networkx as nx
from .phylogenyTree import PhylogenyTree
from .seedmerCreation import create_seedmer
from .seedmer_data import seedmer
from .operationKmer import create_unique_sequences
from .countUniqueSeedmer import count_unique_sequences

class Phylogeny:
    def __init__(self, taxadb_csv, refseq_csv):
        self.taxadb_csv = taxadb_csv
        self.refseq_csv = refseq_csv

    def uniqueSequence(self, taxid, k):
        # Step 1: Create Phylogeny Tree
        G = PhylogenyTree(self.taxadb_csv, self.refseq_csv)

        # Step 2: Create seedmer for target filenames
        target_filenames = G.get_filenames(taxid)
        for filename in target_filenames:
            create_seedmer(filename, k)

        # Step 3: Perform DFS traversal on the graph
        dfs_order = list(nx.dfs_preorder_nodes(G))
        dfs_order.remove(taxid)  # Exclude the target taxid

        # Step 4: Iterate over filenames in DFS order and create unique sequences
        for node_id in dfs_order:
            filenames = G.get_filenames(node_id)

            # Call create_unique_sequences for each filename
            for filename in filenames:
                create_unique_sequences(filename, k, seedmer)

        # Step 5: Print the remaining k-mers in the seedmer dictionary
        print("Unique k-mers in seedmer:", seedmer)
