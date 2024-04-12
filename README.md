
[![GitHub release](https://img.shields.io/github/release/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/)  ![](https://img.shields.io/bower/v/editor.md.svg) [![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg) [![made-for-VSCode](https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg)](https://code.visualstudio.com/) [![Github all releases](https://img.shields.io/github/downloads/Naereen/StrapDown.js/total.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/) [![GitHub watchers](https://img.shields.io/github/watchers/Naereen/StrapDown.js.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/Naereen/StrapDown.js/watchers/)
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

### Docker Installation

Make sure you have Docker installed on your system. You can download and install Docker from [Docker's official website](https://www.docker.com/get-started).

### Running the Containerized Application

#### 1. Pull the Docker Image

```
docker pull nauniseq
```
#### 2. NoSQL Method
To run the NoSQL method, execute the following command:
Please refer to the individual script files for more detailed comments and explanations of the code.
```
docker run --rm nauniseq no_sql --mongodb-uri <mongodb-uri> --taxid <taxid>

```
#### 3. Phylogeny Analysis
To run the phylogeny analysis method, execute the following command:
```
docker run --rm nauniseq phylogeny --taxadb-csv 'taxadb.csv' --refseq-csv 'refseq.csv' --taxid <taxid> --k <k>
```
Replace <taxid> with the taxonomy ID and <k> with the desired length of k-mer.

### Test Data
For test data you need to clone this repo and use the test data

- taxadb.csv: CSV file containing taxonomy data.
- refseq.csv: CSV file containing reference sequence data.
- url_test.txt: Text file containing FTP links for genome and proteome sequences of Neisseria Gonorrhea. Use the provided parallel command to download the multiple files. ***(This is only works in Ubuntu)***
```
parallel -j ${jobs} wget < ng_url.txt
```

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
