def find_all_starts(seq):
    starts = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            starts.append(i)
    return starts


def find_first_in_register_stop(seq):
    stop_codons = {"TGA", "TAG", "TAA"}
    for i in range(0, len(seq), 3):
        if seq[i:i+3] in stop_codons:
            return i
    return -1


def all_orfs_range(seq):
    stop_codons = {"TGA", "TAG", "TAA"}
    starts = find_all_starts(seq)
    orfs = []

    for start in starts:
        for i in range(start + 3, len(seq), 3):
            codon = seq[i:i+3]
            if codon in stop_codons:
                orfs.append((start, i + 3))
                break

    return orfs


def longest_orf(seq):
    orfs = all_orfs_range(seq)
    if not orfs:
        return ""
    start, stop = max(orfs, key=lambda x: x[1] - x[0])
    return seq[start:stop]
