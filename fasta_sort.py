import sys
from os.path import basename, splitext

from Bio import SeqIO


def print_help():
    help_message = """
Usage:
    python fasta_sort.py <input.fasta> [output.fasta]

Description:
    This script reads a FASTA file, sorts the sequences by length, 
    and writes the sorted sequences to a new FASTA file.

Arguments:
    input.fasta    The path to the input FASTA file.
    output.fasta   (Optional) The path to the output FASTA file. 
                  If not provided, the output will be written to a 
                  file named based on the input filename with the "_sorted" suffix.
    """
    print(help_message)


# Check for no arguments or help flags
if len(sys.argv) == 1 or sys.argv[1] in ["-h", "--help"]:
    print_help()
    sys.exit()

# Define input and output file
fasta_file = sys.argv[1]
# Output is name_sorted.fasta unless a second output name is specified
output_file = (
    sys.argv[2]
    if len(sys.argv) > 2
    else f"{splitext(basename(fasta_file))[0]}_sorted.fasta"
)

# Read sequences from FASTA file
with open(fasta_file, "r") as in_file:
    sequences = list(SeqIO.parse(in_file, "fasta"))
    print(f"Sorting {len(sequences)} sequences from {fasta_file}")

# Sort sequences by length
sorted_sequences = sorted(sequences, key=lambda seq: len(seq))

# Write sorted sequences to a new FASTA file
print(f"Saving to {output_file}")
with open(output_file, "w") as out_file:
    SeqIO.write(sorted_sequences, out_file, "fasta")
