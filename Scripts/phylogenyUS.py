import click,os,json,progressbar
import networkx as nx
from .phylogenyTree import PhylogenyTree
from .seedmerCreation import create_seedmer
from .seedmer_data import seedmer
from .operationKmer import create_unique_sequences
from .countUniqueSeedmer import count_unique_sequences

class Phylogeny:
    path = '/app/test_data'
    def __init__(self, taxadb_csv, refseq_csv):
        self.taxadb_csv = os.path.join(Phylogeny.path,taxadb_csv)
        self.refseq_csv = os.path.join(Phylogeny.path,refseq_csv)

    def uniqueSequence(self, taxid, k):
        # Step 1: Create Phylogeny Tree
        G = PhylogenyTree()
        graph = G.create_graph(self.taxadb_csv, self.refseq_csv)
        print('*********************************')
        print('Phylogeny Tree is Created')
        # Step 2: Create seedmer for target filenames
        target_filenames = G.get_filenames(graph,taxid)
        target_progress = progressbar.ProgressBar(max_value=len(target_filenames))
        print('*********************************')        
        print("Creating Seedmer...")
        for i,filename in enumerate(target_filenames):
            create_seedmer(filename, k)
            target_progress.update(i + 1)
        print('*********************************')        
        print("Seedmer is created")
        print("Total length of seedmer : ",len(seedmer))
        # Step 3: Perform DFS traversal on the graph
        dfs_order = list(nx.dfs_preorder_nodes(graph))
        dfs_order.remove(taxid)  # Exclude the target taxid
        print('Perform DFS')
        print("******************************")
        non_target_progress = progressbar.ProgressBar(max_value=len(dfs_order))
        print("Creating unique sequences...")
        print('*********************************')
        # Step 4: Iterate over filenames in DFS order and create unique sequences
        for i,node_id in enumerate(dfs_order):
            filenames = G.get_filenames(graph,node_id)
            if not filenames:
                continue
            # Call create_unique_sequences for each filename
            for filename in  filenames:
                create_unique_sequences(filename, k)
            non_target_progress.update(i+1)
        # Step 5: Print the remaining k-mers in the seedmer dictionary
        print('*********************************')
        print("Unique k-mers in seedmer:", seedmer)
        print("Length of new seedmer",len(seedmer))
