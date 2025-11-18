def find_all_starts(seq):
    starts = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            starts.append(i)
    return starts


def find_first_in_register_stop(seq, start_index):
    stop_codons = {"TGA", "TAG", "TAA"}
    
    for i in range(start_index + 3, len(seq), 3):
        codon = seq[i:i+3]
        if codon in stop_codons:
            return i
    return -1


def all_orfs_range(seq):
    orfs = []
    starts = find_all_starts(seq)
    
    for start in starts:
        stop = find_first_in_register_stop(seq, start)
        if stop != -1:
            orfs.append((start, stop + 3))
    return orfs


def longest_orf(seq):
    orfs = all_orfs_range(seq)
    if not orfs:
        return ""
    
    longest = max(orfs, key=lambda x: x[1] - x[0])
    start, stop = longest
    return seq[start:stop]
