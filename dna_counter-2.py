# DNA Nucleotide Counter
# Author: Aliya Khan
# Description: Counts A, T, G and C nucleotides in a DNA sequence.

def count_nucleotides(sequence):
    sequence = sequence.upper().replace(" ", "").replace("\n", "")

    # Validate DNA sequence
    if not sequence or any(base not in "ATGC" for base in sequence):
        return None

    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }

    return counts


sequence = input("Enter DNA sequence: ")

result = count_nucleotides(sequence)

if result:
    print("\nDNA Nucleotide Count")
    print("--------------------")
    for nucleotide, count in result.items():
        print(f"{nucleotide}: {count}")

    print(f"Total nucleotides: {sum(result.values())}")
else:
    print("Invalid DNA sequence! Please use only A, T, G and C.")
