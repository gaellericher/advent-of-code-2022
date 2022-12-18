from os.path import join, dirname
from collections import Counter
import re

def is_a_marker(seq, marker_size):
    counts = Counter(seq)
    for c, count in counts.items():
        if count > 1:
            return False, seq.index(c)+1
    return True, 0
            
def find_marker(ds, marker_size=4):
    i = 0
    found = False
    while not found and i+marker_size <= len(ds):
        found, offset = is_a_marker(ds[i:i+marker_size], marker_size)
        i += offset
    return i+marker_size if found else None
    

if __name__ == '__main__':
    with open(join(dirname(__file__), "input"), "r") as f:
        stream = f.readlines()[0]

        print(
            f"[Day 6] Processed characters after marker (1st part): {find_marker(stream, marker_size=4)}, "
            f"Processed characters after marker (1st part): {find_marker(stream, marker_size=14)}"
        )
