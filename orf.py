def find_all_starts(seq):
    starts = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            starts.append(i)
    return starts

def all_orfs_range(seq):
    orfs = []
    starts = find_all_starts(seq)
    for start in starts:
        for i in range(start + 3, len(seq) - 2, 3):
            codon = seq[i:i+3]
            if codon in {"TGA", "TAG", "TAA"}:
                orfs.append((start, i + 3))
                break
    return orfs

def longest_orf(seq):
    orfs = all_orfs_range(seq)
    if not orfs:
        return ""
    start, stop = max(orfs, key=lambda x: x[1] - x[0])
    return seq[start:stop]
