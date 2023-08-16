# UMLS-Data-Cleaning

This repository was made to contribute to a GPT Benchmarking research project as part of the 2023 Data Science Summer Fellowship at the University of California, Riverside. 

The goal of the code in this repository is to organize and extract certain data fields from the MRCONSO and MRREL files from the Unified Medical Language System (https://www.nlm.nih.gov/research/umls/index.html).
This is done with the end goal to streamline and automate diverse query generation from medical information. 

The main content of this repository can be found in the 'Python Scripts' folder, which contains scripts that are an extension of the .ipynb code in the 'Notebook Code' folder.

The MRCONSO script extracts all the unique names of drugs and/or diseases found in the file, along with giving the user the option to get a single drug/disease name either from a specified index or at random.
The MRREL script gives the user the option to extract all the information for a specific relationship in the file, or to extract all of the information for each of the relationships in the entire file. 
