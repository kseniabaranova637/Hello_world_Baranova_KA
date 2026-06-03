files = ["seq1", "seq2", "seq3", "seq4"]
data = ".21.01.2008"
for name in files:
    new_name = name + ".fasta"
    two_name = new_name + data
    print(f"{two_name}")