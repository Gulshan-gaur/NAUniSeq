import click,os,json
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
        print('Phylogent Tree is Created')
        # Step 2: Create seedmer for target filenames
        target_filenames = G.get_filenames(taxid)
        for filename in target_filenames:
            create_seedmer(filename, k)
        with open('app/seedmer.txt','w') as json_file:
            json.dump(seedmer,json_file)
        print('*********************************')        
        print("Seedmer is craeted")
        print("Total lenght of seedmer : ",len(seedmer))
        # Step 3: Perform DFS traversal on the graph
        dfs_order = list(nx.dfs_preorder_nodes(graph))
        dfs_order.remove(taxid)  # Exclude the target taxid
        print('Perform DFS')
        print("******************************")
        # Step 4: Iterate over filenames in DFS order and create unique sequences
        for node_id in dfs_order:
            filenames = G.get_filenames(graph,node_id)
            if not filenames:
                continue
            # Call create_unique_sequences for each filename
            for filename in filenames:
                create_unique_sequences(filename, k)
        os.remove('app/seedmer.txt')
        with open('app/seedmer.txt','w') as json_file:
            json.dump(seedmer,json_file)
        # Step 5: Print the remaining k-mers in the seedmer dictionary
        print("Unique k-mers in seedmer:", len(seedmer))
