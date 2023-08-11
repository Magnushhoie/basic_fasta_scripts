# biopython_fasta_scripts
This repository contains basic standalone scripts for processing FASTA files in various ways using Biopython. Below are brief descriptions and usage examples for each script:

Usage:
```bash
# fasta_sort.py - Sort FASTA by length
python fasta_sort.py input.fasta [output.fasta]
# Example: Sort from shortest to longest sequence
python fasta_sort.py sequences.fasta sorted_sequences.fasta

# fasta_uniq.py - Remove FASTA duplicates
python fasta_uniq.py input.fasta [output.fasta]
# Example: removes duplicated FASTA entries or sequences
python fasta_uniq.py sequences.fasta unique_sequences.fasta

# fasta_splitlen.py - Split FASTA by sequence length
python fasta_splitlen.py input.fasta --lengths LENGTHS
# Example: split at lengths 0-49, 50-99 and 100plus
python fasta_splitlen.py sequences.fasta --lengths "50,100"

# fasta_splitevery.py - Split FASTA every n entries
python fasta_splitevery.py input.fasta --count COUNT
# Example: Split into new file every 2 sequences
python fasta_splitevery.py sequences.fasta --count 2
```

Requirements:
```bash
pip install biopython
```
