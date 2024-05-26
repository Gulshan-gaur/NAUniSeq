import pandas as pd
import networkx as nx
import os

class PhylogenyTree:
    def __init__(self, taxadb_csv, refseq_csv):
        self.taxadb_csv = taxadb_csv
        self.refseq_csv = refseq_csv
        self.graph = self._create_graph()
        
    def _create_graph(self):
        # Read the taxadb CSV file
        taxadb_df = pd.read_csv(self.taxadb_csv)

        # Read the refseq database CSV file
        refseq_df = pd.read_csv(self.refseq_csv)

        # Create an empty graph
        graph = nx.DiGraph()

        # Add nodes to the graph
        for _, row in taxadb_df.iterrows():
            taxid = row['taxid']
            parent_id = row['parent_taxid']
            
            # Get the filenames for the current taxid
            filenames = refseq_df[refseq_df['taxid'] == taxid]['link'].apply(os.path.basename).tolist()

            # Create a dictionary of attributes for the node
            attributes = {
                'filenames': filenames,
                'ftp_links': refseq_df[refseq_df['taxid'] == taxid]['ftp_path'].tolist(),
                'assembly_levels': refseq_df[refseq_df['taxid'] == taxid]['assembly_level'].tolist()
            }

            graph.add_node(taxid, **attributes)
            graph.add_edge(parent_id, taxid)
        
        # Return the phylogenetic graph
        return graph

    def get_filenames(self, taxid):
        return self.graph.nodes[taxid]['filenames']