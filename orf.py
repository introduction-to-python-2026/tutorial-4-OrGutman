def find_all_starts(seq):
    starts = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            starts.append(i)
    return starts


def find_first_in_register_stop(seq):
    stop_codons = {"TGA", "TAG", "TAA"}
    n = len(seq)

    for i in range(0, n - 2):
        codon = seq[i:i+3]

        if codon in stop_codons:
            if (n - (i + 3)) % 3 == 0:
                return i

    return -1


def all_orfs_range(seq):
    orfs = []
    starts = find_all_starts(seq)

    for start in starts:
        stop_index = find_first_in_register_stop(seq[start:])
        
        if stop_index != -1:
            stop_index = start + stop_index
            orfs.append((start, stop_index + 3))

    return orfs


def longest_orf(seq):
    orfs = all_orfs_range(seq)
    if not orfs:
        return ""
    
    start, stop = max(orfs, key=lambda x: x[1] - x[0])
    return seq[start:stop]
