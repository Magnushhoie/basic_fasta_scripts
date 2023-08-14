# basic_fasta_scripts
This repository contains basic standalone scripts for processing FASTA files in various ways using Biopython. Below are brief descriptions and usage examples for each script:

Usage:
```bash
# fasta_sort.py - Sort from shortest to longest sequence
python fasta_sort.py input.fasta [output.fasta]
python fasta_sort.py sequences.fasta sorted_sequences.fasta

# fasta_uniq.py - Removes duplicated FASTA entries or sequences
python fasta_uniq.py input.fasta [output.fasta]
python fasta_uniq.py sequences.fasta unique_sequences.fasta

# fasta_splitlen.py - Split into new FASTA files by sequence lengths (e.g. 0-49, 50-99, 100+)
python fasta_splitlen.py input.fasta --lengths LENGTHS
python fasta_splitlen.py sequences.fasta --lengths "50,100"

# fasta_splitevery.py - Split into new FASTA files every n entries (e.g. every 2)
python fasta_splitevery.py input.fasta --count COUNT
python fasta_splitevery.py sequences.fasta --count 2
```

Requirements:
```bash
pip install biopython
```
