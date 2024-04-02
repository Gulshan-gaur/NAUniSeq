import click
from Scripts.noSql import NoSql
from Scripts.phylogenyUS import Phylogeny

@click.group()
def main():
    pass

@main.command()
@click.option('--mongodb-uri', default='mongodb://localhost:27017/', help='MongoDB URI')
@click.option('--taxid', type=int, help='Taxonomy ID')
@click.option('--k', type=int, default=100, help='Length of k-mer')
def no_sql(mongodb_uri,taxid,k):
    """Run the NoSQL method."""
    # Initialize and run the NoSQL method
    no_sql_method = NoSql(mongodb_uri)
    no_sql_method.uniqueSequence(taxid,k)

@main.command()
@click.option('--taxadb-csv', default='taxadb.csv', help='Path to the taxadb CSV file')
@click.option('--refseq-csv', default='refseq.csv', help='Path to the refseq CSV file')
@click.option('--taxid', type=int, help='Taxonomy ID')
@click.option('--k', type=int, default=100, help='Length of k-mer')
def phylogeny(taxadb_csv, refseq_csv, taxid, k):
    """Run the phylogeny analysis."""
    # Initialize and run the phylogeny analysis
    phylogeny_analysis = Phylogeny(taxadb_csv, refseq_csv)
    phylogeny_analysis.uniqueSequence(taxid, k)

if __name__ == "__main__":
    main()
