
[![GitHub release](https://img.shields.io/github/release/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/)  ![](https://img.shields.io/bower/v/editor.md.svg) [![made-for-VSCode](https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg)](https://code.visualstudio.com/) [![Github all releases](https://img.shields.io/github/downloads/Naereen/StrapDown.js/total.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/) [![GitHub watchers](https://img.shields.io/github/watchers/Naereen/StrapDown.js.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/Naereen/StrapDown.js/watchers/)
[![git](https://badgen.net/badge/icon/git?icon=git&label)](https://git-scm.com) [![Visual Studio Code](https://img.shields.io/badge/--007ACC?logo=visual%20studio%20code&logoColor=ffffff)](https://code.visualstudio.com/) [![PyPi](https://badgen.net/badge/icon/pypi?icon=pypi&label)](https://https://pypi.org/)

   
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### Project Title

A brief description of what this project does and who it's for

NAUniSeq: A fast computational pipeline to search unique sequences for microbial diagnostics

### NAUniSeq Manual
1. Introduction
2. Principle of operation
3. Download of sequence data
4. Collection in MongoDB
5. K-mer strategies
6. Generation of unique sequences

### Introduction
NAUniSeq (short for Nucleotide and Amino Acid unique sequences) pipeline was developed to search for unique nucleotide and amino acid sequences. The original aim was to find unique sites to design primers, probes, antigenic sites for specific detection of microorganism. It takes target ("microorganism for which we want to find nucleotide and amino acid unique sequences") and non-target (Complete genome and protein sequences taken from NCBI Refseq FTP server minus target sequence) sequences, generates their K-mers and cross referencing them finds unique sequences that are unique for target genome(s).
The purpose of our pipeline is to find unique sequences for diagnostic use. Although possible use cases are not limited, Use of our pipeline can be extended to plant diseases also. We have used this method for designing unique sequences of nucleotides and amino acids but this pipeline is also applicable for designing unique RNA sequences. Complete transcriptomic data can be downloaded as rna.fna.gz files from NCBI Refseq. 


### System requirement and dependencies

For the present study we have used a desktop system with configurations: Intel core i7 10700K, PCI Graphics Card RTX 1660 and RAM 16 GBx2. Aim of the present invention was to provide a pipeline named NAUniSeq, implemented in the Python 3.7 programming language and ran on the Linux or Unix command line. Ubuntu 20.04, MongoDB 5.0.6 and VS Code 1.67.2 versions were used in the development of this pipeline. 

### Repository Contents
# Phylogeny Analysis Code Repository

This repository contains code for analyzing phylogenetic data using a combination of network analysis, seedmer creation, and unique sequence generation. The code is implemented in Python and utilizes various libraries for data processing and analysis.

## Usage
#### Note : Run all the command in ubuntu to save yourself from any error.

### Clone this repo
```
git clone https://github.com/Gulshan-gaur/NAUniSeq.git 
```

### Use cd to naviagte to the test_data folder from where you have cloned the repo
```
cd $(pwd)/NAUniSeq/test_data
```
### Test Data
In test_data folder

- taxadb.csv: CSV file containing taxonomy data.
- refseq.csv: CSV file containing reference sequence data.
- ng_url.txt: Text file containing FTP links for genome sequences of Neisseria Gonorrhea. 
- genome files in compress gzip for Neisseria gonorrhoeae and it's adjcent neighbours or child it has 783 files of Neisseria gonorrhoeae and 87 for child or neighbours

#### Note : you need to download the test_data folder from [here](https://labs4research-my.sharepoint.com/:u:/g/personal/gaurgulshan_sigmamind_xyz/EVkEVSi35GRNo0H0dnSweKgBu2oLssvdwoVgZk12UvOIew?e=YyXkfc) it is in zip, replace this test_data folder after unzip with test_data.



### Add data to mongoDb database (if you want to run nosql method)
Make sure you have MongoDb installed on your system and start the service before running.
```
#install the pymongo and pandas with pip
pip install pymongo pandas
```
Run the insert_refseq_to_mongodb.py to add refseq data to your local instance of mongodb
```
python insert_refseq_to_mongodb.py
```
### Docker Installation

Make sure you have Docker installed on your system. You can download and install Docker from [Docker's official website](https://www.docker.com/get-started).

### Running the Containerized Application

#### 1. Pull the Docker Image

```
docker pull gaurgulshan/nauniseq:latest
```
#### 2. Tag the image with just the repository name: 
```
docker tag gaurgulshan/nauniseq:latest nauniseq:latest
```
#### 3. NoSQL Method
To run the NoSQL method, execute the following command:
Please refer to the individual script files for more detailed comments and explanations of the code.
```
docker run --network="host" -v $(pwd)/test_data:/app/test_data -it nauniseq python main.py no-sql --mongodb-uri 'mongodb://localhost:27017/' --taxid 485 --k 100

```
For windows you need to replace with full path of the folder.
```
docker run --network="host" -v C:/Users/YourUsername/Documents/NAuniseq/test_data:/app/test_data -it nauniseq python main.py no-sql --mongodb-uri "mongodb://localhost:27017/" --taxid 485 --k 100

```
#### 4. Phylogeny Analysis
To run the phylogeny analysis method, execute the following command:
```
docker run -v $(pwd)/test_data:/app/test_data -it nauniseq python main.py phylogeny --taxadb-csv 'taxa_db.csv' --refseq-csv 'refseq.csv' --taxid 485 --k 100

```
For windows you need to replace with full path of the folder.
```
docker run -v C:/Users/YourUsername/Documents/NAuniseq/test_data/test_data:/app/test_data -it nauniseq python main.py phylogeny --taxadb-csv 'taxa_db.csv' --refseq-csv 'refseq.csv' --taxid 485 --k 100
```
### Sensitivity and Specificity Calculation : 
#### We have analyzed the results from the positive and negative databases using local BLAST with clinical isolates. For the calculation of sensitivity and specificity, we consider those sequences that align with the query sequences (Unique sequences from our method NOSql and Phylogeny) (which are unique sequences) and have an alignment percentage of 98% to 100%. This rigorous criterion ensures that only high-confidence matches are taken into account. By focusing on these stringent alignment thresholds, we ensure accurate assessment of our nucleotide markers' performance. you can find more explaination [here](https://github.com/Gulshan-gaur/NAUniSeq/blob/main/blast.md)

### Sensitivity and Specificity Table

| Identifier | Sequence | Sensitivity | Specificity |
|------------|-----------|-------------|-------------|
| s1 | TACCGAAGCACCTGCCGCCGAAGCTGCTGCTACCGAAGCACCTGCCGCCGAAGCTGCTGCTACCGAAGCACCTGCCGCCGAAGCTGCTGCTACCGAAGCA | 71.00 | 100 |
| s2 | CAGGTAAAGCGTGTTTCTTGACAAGTTAAACGTTGCTGCGGTTTGACCGGTGTTTTTGCATTGTCCGTAATATAGCGGATTAACAAAAACCGGTACGGCG | 85.00% | 100 |
| s3 | AATCGAATCGGGTGCGAACGACCCGATGGCGGTTTTTTTTGGTTACGGCACTGATTACCATGATTATGCAGCCGGCGGAATCGGGTGCGGCAGCGTTTGT | 83.33% | 100 |
| s4 | ACAGGGCGGTCAGGAGCGCGGAGGCGGCGGCGTATAGGGAAACCGTCCGCCGTATCGCGCAAGGGGCGGGCGCGATGCCGTCCGAAGGCTTTGTGGCGGT | 98.17% | 100 |
| s5 | TCGCCCGGTGCTTGGGCGCCTTAGGGAATCGTTCCCTTTGAGCCGGGGCGGGGCAACGCCGTACCGGTTTTTGTTAATCCGCTATAATTTTAAGGTTTGC | 100 | 99.94 |
| s6 | ACGGCAAATGGCCCGCCGACAACGGCGCTGCCGGCGTGGCATCCTCCGCCGAAATCAAAGGCAAATATGTTCAGAAAGTTGAAGTCGCAAAAGGCGTCG | 81.67 | 100 |
| s7 | CGCCATCGCCCGCGTGATGCTCAAAGACGCACCCATCCTGCTGCTTGACGAAGCCACCAGCACGCTCGATTCCGAAGTTGAAGCCGCCATCCAAGAAAGC | 83.33 | 99.99 |
| s8 | GTTTACAGCTATGGTTTCAGCGAACACGCCGACATCCGCATTACCGATTTCACCGCCTCTTCAGACGGCATAGAAGCCGTATTCCGAACCCCGTGGGGCG | 83.33 | 100 |
| s9 | AGGTTCAGACGGCATTGGAATCGGGGGATCAGAAGCGGTAGCGCACGCCCAACGAGGCTTCGTGGGTTTTGAAGCGGGTGTTTTCCAAGCGTCCCCAGTT | 100 | 100 |
| s10 | CCCGCAGCCTGTCCCTGATCCGCGCGTCGGTGTTTTTCGCGGAAGGCTTCCGCCGTCAGGTTGGTCAGCACCAGCATCGGCATCAGCCGCTCGTACCGGG | 98.67 | 99.98 |


## Repository Structure

- `noSql.py`: This script implements the NoSQL approach for phylogeny analysis using MongoDB as the database. It connects to the MongoDB server, retrieves taxonomic and genomic data, and performs the necessary steps for seedmer creation and unique sequence generation.

- `operationKmer.py`: This module provides functions related to k-mer operations, such as creating seedmers and generating unique sequences.

- `phylogenyTree.py`: This module defines the PhylogenyTree class, which represents the phylogenetic tree and provides methods for accessing taxonomic and genomic data.

- `phylogenyUS.py`: This script implements the phylogeny analysis using the PhylogenyTree class. It creates the phylogenetic tree, performs seedmer creation and unique sequence generation for target and non-target taxa, and displays the unique k-mers.

- `seedmer_data.py`: This module defines the seedmer dictionary, which stores k-mers and their associated information.

- `seedmerCreation.py`: This module contains the function for creating seedmers from genomic files using a sliding window technique.

- `countUniqueSeedmer.py` : This module can count the unique sequence that are ovarlapped.

- `qblast.py` : Performing for blastp and blastn 

- `README.md`: This file provides an overview of the code repository, its structure, and usage instructions.


### Authors

- Dr. Vandana Nunia
- [@Gulshan-gaur](https://www.github.com/Gulshan-gaur)
- Rakesh Sharma


### Licence

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

#### We Build The Future❤️
![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)

Please let me know if you need any further assistance!
