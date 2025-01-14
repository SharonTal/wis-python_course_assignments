




# This program analyzes sequences from Fasta or GeneBank files. It supports two analyses:
# 1. Finding the longest duplicated subsequence.
# 2. Finding the most common k-mer (substring of specified length)


import argparse
from Bio import SeqIO

def find_longest_duplicate(sequence):
    """Find the longest subsequence that repeats itself."""
    n = len(sequence)
    longest = ""
    
    for i in range(n):
        for j in range(i + 1, n):
            k = 0
            while j + k < n and sequence[i + k] == sequence[j + k]:
                k += 1
            if k > len(longest):
                longest = sequence[i:i + k]
    
    return longest

def most_common_kmer(sequence, k=3):
    """Find the most common k-mer in the sequence."""
    kmer_counts = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1

    most_common = max(kmer_counts, key=kmer_counts.get)
    return most_common, kmer_counts[most_common]

def parse_fasta_genbank(file_path):
    """Parse a Fasta or GeneBank file and return the sequence."""
    try:
        record = next(SeqIO.parse(file_path, "fasta"))
    except Exception:
        record = next(SeqIO.parse(file_path, "genbank"))
    return str(record.seq)

def main():
    parser = argparse.ArgumentParser(description="Analyze sequences from Fasta or GeneBank files.")
    parser.add_argument("file", help="Path to the Fasta or GeneBank file.")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest duplicated subsequence.")
    parser.add_argument("--kmer", type=int, help="Find the most common k-mer of the specified length.")

    args = parser.parse_args()

    sequence = parse_fasta_genbank(args.file)

    if args.duplicate:
        longest_duplicate = find_longest_duplicate(sequence)
        print(f"Longest duplicated subsequence: {longest_duplicate}")

    if args.kmer:
        kmer, count = most_common_kmer(sequence, k=args.kmer)
        print(f"Most common {args.kmer}-mer: {kmer} (Count: {count})")

if __name__ == "__main__":
    main()
