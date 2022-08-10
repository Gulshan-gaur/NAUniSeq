
[![GitHub release](https://img.shields.io/github/release/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/)  ![](https://img.shields.io/bower/v/editor.md.svg) [![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg) [![made-for-VSCode](https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg)](https://code.visualstudio.com/) [![Github all releases](https://img.shields.io/github/downloads/Naereen/StrapDown.js/total.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/) [![GitHub watchers](https://img.shields.io/github/watchers/Naereen/StrapDown.js.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/Naereen/StrapDown.js/watchers/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)               
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
NAUniSeq (short for Nucleotide and Amino Acid unique sequences) pipeline was developed to search for unique nucleotide and amino acid sequences. The original aim was to find unique sites to design primers, probes, antigenic sites for specific detection of microorganism. It takes target ("microorganism for which we want to find nucleotide and amino acid unique sequences") and non-target (Complete genome and protein sequences taken from NCBI Refseq FTP server minus target sequence) sequences, generates their K-mers and cross referencing them finds unique sequences that are unique for target genome(s). NCBI provides a Refseq database (reference sequences) for taxonomically diverse organisms including archaea, bacteria, eukaryotes, and viruses. We performed a K-mer operation and got multiple unique sequences. Further, we run the NCBI blast programme to select the fragments that were specific for the strain. For the amino acid unique sequences, we checked the complete protein and with the help of online tools only membrane proteins were selected. Further their antigenic potential was also determined. These target unique sequences were stored in MongoDB unique sequence collection. 
The purpose of our pipeline is to find unique sequences for diagnostic use. Although possible use cases are not limited, Use of our pipeline can be extended to plant diseases also. We have used this method for designing unique sequences of nucleotides and amino acids but this pipeline is also applicable for designing unique RNA sequences. Complete transcriptomic data can be downloaded as rna.fna.gz files from NCBI Refseq. 

### Principle of operation

NAUniSeq pipeline is designed to use complete genome and protein data from NCBI Refseq FTP server as non-target and target microorganism to find unique sequences in target. The principle of NAUniSeq pipeline can be divided into 3 main stages: Data download from NCBI Refseq FTP server, creation of downloaded sequences collection in MongoDB and K-mer operation that includes 1. generation of target and non-target K-mers 2. cross referencing of the K-mers 3. storage of unique K-mers in MongoDB 
In the first stage we have downloaded data from NCBI refseq FTP serever. To download data from RefSeq database a schema was designed. 
* **Assembly Dataframe**

![Assembly Dataframe](https://github.com/Gulshan-gaur/NAUniSeq/blob/main/images/Assembly.png)

From this refseq assembly file we have extracted columns that have FTP links (https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/905/GCF_000001905.1_Loxafr3.0/). We have split this link and taken the last index string and added /genomic.fna.gz for genomes and /_protein.faa.gz for proteins to all the FTP links and downloaded them to our local system as a text file.
* **Ftp Links**

![Ftp links](https://github.com/Gulshan-gaur/NAUniSeq/blob/main/images/links.png)
 
In the second stage downloaded genome and protein sequeneces were added to the MongoDB documents. We have designed five key value pair data schemas of MongoDB collection. A schema is a JSON object that defines the structure and contents of our data. First key was the node which was the tax-id column (data type: integer), second key was accession number, third was FTP link, fourth was file path which was the local file system path of genomic files and fifth key was assembly level. After that we have added the local system file path to every specific sequence file. MongoDB also gives us 24 characters unique id, which is usually auto generated. 
* **MongoDB Collection**
```
{

    "*_id": "objectId",
    "tax_id": "int",
    "assembly_level":  "string" ,
    "accession no.":  "string" ,
    "file _path":  "string" ,
    "ftp_link": "string" 
}
```
*Auto generated unique id,12 bytes and 24 in length
* **Genomic Collection**

![MongoDb collection](https://github.com/Gulshan-gaur/NAUniSeq/blob/main/images/mongodb.png)

In the third step we ran a K-mer operation to check whether the non-target kmers are present in target K-mers or not. A genome and protein of size N were fragmented into N-K+1 fragments. In this function target and non-target K-mers were cross-referenced, target K-mers present in non-target collections were removed. If the non-target k-mers were present in target K-mer we excluded those K-mers. Now at the same time we checked the old length of the target K-mer text file with the current length. If the current seedmer length was not equal to the old length of seedmer then we deleted the old seedmer file and we have dumped the new seedmer object to seedmer.json file. These target unique sequences were stored in MongoDB unique sequence collection. 
For unique nucleotide K-mers NCBI-blast was run to get only strain specific fragments. For amino acid K-mers, complete protein sequences of unique length fragments were further run in the protein plasma membrane prediction tools and K-mers predicted to be in the plasma membrane were selected. These K-mers were further checked for their antigenic potential.
* **K-mer strategies**
##### **Nuclotide Kmer**
![ DNA kmer ](https://github.com/Gulshan-gaur/NAUniSeq/blob/main/images/Dna%20Kmer.jpg)
##### Amino Acid Kmer
![Amino acid kmer](https://github.com/Gulshan-gaur/NAUniSeq/blob/main/images/Peptide%20Kmer.jpg)

### System requirement and dependencies

For the present study we have used a desktop system with configurations: Intel core i7 10700K, PCI Graphics Card RTX 1660 and RAM 16 GBx2. Aim of the present invention was to provide a pipeline named NAUniSeq, implemented in the Python 3.7 programming language and ran on the Linux or Unix command line. Ubuntu 20.04, MongoDB 5.0.6 and VS Code 1.67.2 versions were used in the development of this pipeline. 

### Repository Contents

### Authors

- Dr. Vandana Nunia
- [@Gulshan-gaur](https://www.github.com/Gulshan-gaur)
- Rakesh Sharma


### Licence

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

#### We Build The Future❤️
![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)
