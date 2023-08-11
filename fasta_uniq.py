import sys
from os.path import basename, splitext

from Bio import SeqIO


def print_help():
    help_message = """
Usage:
    python fasta_uniq.py <input.fasta> [output.fasta]

Description:
    This script reads a FASTA file and removes entries with duplicate headers or sequences,
    then writes the unique entries to a new FASTA file.

Arguments:
    input.fasta    The path to the input FASTA file.
    output.fasta   (Optional) The path to the output FASTA file. 
                  If not provided, the output will be written to a 
                  file named based on the input filename with the "_unique" suffix.
    """
    print(help_message)


# Check for no arguments or help flags
if len(sys.argv) == 1 or sys.argv[1] in ["-h", "--help"]:
    print_help()
    sys.exit()

# Define input and output file
fasta_file = sys.argv[1]
# Output is name_unique.fasta unless a second output name is specified
output_file = (
    sys.argv[2]
    if len(sys.argv) > 2
    else f"{splitext(basename(fasta_file))[0]}_unique.fasta"
)

# Read sequences from FASTA file
with open(fasta_file, "r") as in_file:
    sequences = list(SeqIO.parse(in_file, "fasta"))
    print(f"Processing {len(sequences)} sequences from {fasta_file}")

# Remove duplicates based on header and sequence
unique_records = []
seen_headers = set()
seen_sequences = set()

for record in sequences:
    if record.id not in seen_headers and str(record.seq) not in seen_sequences:
        unique_records.append(record)
        seen_headers.add(record.id)
        seen_sequences.add(str(record.seq))

# Write unique records to a new FASTA file
print(f"Saving {len(unique_records)} unique records to {output_file}")
with open(output_file, "w") as out_file:
    SeqIO.write(unique_records, out_file, "fasta")
