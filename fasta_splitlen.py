import argparse
from argparse import ArgumentParser, RawTextHelpFormatter
from os.path import basename, splitext

from Bio import SeqIO


def cmdline_args():
    # Make parser object
    usage = f"""
    Usage:
        python fasta_splitlen.py input_file --lengths "LENGTHS"

    Description:
        Split a FASTA file based on sequence length. Sequences are distributed into buckets based 
        on their length and written to separate output files.

    Examples:
        # Split into lengths 0-49 and 50+
        python script_name.py example.fasta --lengths "50"

        # Split into lengths 0-49, 50-99 and 100+
        python script_name.py example.fasta --lengths "50,100"

    """
    p = ArgumentParser(
        description="fasta_splitlen.py",
        formatter_class=RawTextHelpFormatter,
        usage=usage,
    )
    p.add_argument("input_file", help="Input FASTA file.")
    p.add_argument(
        "--lengths",
        type=str,
        required=True,
        help="Comma-separated length thresholds, e.g., '60,90,120'.",
    )

    return p.parse_args()


def distribute_sequences(sequences, lengths):
    buckets = {length: [] for length in lengths}
    buckets["plus"] = []

    for seq in sequences:
        placed = False
        for i, length in enumerate(lengths):
            if len(seq) < length:
                buckets[length].append(seq)
                placed = True
                break

        if not placed:
            buckets["plus"].append(seq)

    return buckets


def read_fasta_entries(filename):
    with open(filename, "r") as f:
        sequences = list(SeqIO.parse(f, "fasta"))
    print(f"Read {len(sequences)} sequences from {filename}")
    return sequences


def write_fasta_entries(entries, filename):
    if not entries:
        print(f"No entries for {filename}")
    else:
        print(f"Writing {len(entries)} sequences to {filename}")
        with open(filename, "w") as f:
            SeqIO.write(entries, f, "fasta")


def main():
    # Argument parsing
    args = cmdline_args()

    # Get lengths to use
    lengths = sorted([int(l) for l in args.lengths.split(",")])
    base_name = splitext(basename(args.input_file))[0]

    # Read sequences
    sequences = read_fasta_entries(args.input_file)

    # Distribute sequences into buckets
    buckets = distribute_sequences(sequences, lengths)

    # Write sequences from each bucket to separate files
    previous_threshold = 0
    for length in lengths:
        write_fasta_entries(
            buckets[length],
            filename=f"{base_name}_length_{previous_threshold}-{length-1}.fasta",
        )
        previous_threshold = length

    # Write sequences longer than the last length threshold
    write_fasta_entries(
        buckets["plus"], filename=f"{base_name}_length_{lengths[-1]}plus.fasta"
    )


if __name__ == "__main__":
    main()
