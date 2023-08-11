from argparse import ArgumentParser, RawTextHelpFormatter
from os.path import basename, splitext

from Bio import SeqIO


def cmdline_args():
    # Make parser object
    usage = f"""
    Usage:
        python fasta_splitevery.py input_file --count COUNT

    Description:
        Splits a FASTA file into multiple smaller files, each containing a specified number of sequences.


    Examples:
        # Split off at every 5 entries
        python script_name.py example.fasta --count "5"
    """
    p = ArgumentParser(
        description="fasta_splitevery.py",
        formatter_class=RawTextHelpFormatter,
        usage=usage,
    )
    p.add_argument("input_file", help="Input FASTA file.")
    p.add_argument(
        "--count", type=int, required=True, help="Number of sequences per file."
    )

    return p.parse_args()


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

    base_name = splitext(basename(args.input_file))[0]

    # Read sequences
    sequences = read_fasta_entries(args.input_file)

    # Warn the user if more than 10 files will be created
    num_files = len(sequences) // args.count + (
        1 if len(sequences) % args.count != 0 else 0
    )
    if num_files > 1:
        input(
            f"Warning: This will create {num_files} files. Press Enter to continue or Ctrl+C to abort."
        )

    # Split sequences and write to files
    for i in range(0, len(sequences), args.count):
        write_fasta_entries(
            sequences[i:i + args.count],
            filename=f"{base_name}_{i}-{i + args.count}.fasta",
        )   


if __name__ == "__main__":
    main()
