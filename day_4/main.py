from os.path import join, dirname

def parse_pair(pair):
    return [[int(x) for x in p.split("-")] for p in pair.split(",")]

def interval_is_contained(a, b, i, j):
    return a <= i and b >= j

def interval_overlap(a, b, i, j):
    return i <= a <= j or i <= b <= j

def contains(interval1, interval2):
    return interval_is_contained(*interval1, *interval2) or \
        interval_is_contained(*interval2, *interval1)

def overlap(interval1, interval2):
    return interval_overlap(*interval1, *interval2) or \
        interval_overlap(*interval2, *interval1)

def filter_assignment_pairs(pairs, filter):
    return [pair for pair in pairs if filter(*parse_pair(pair))]

if __name__ == '__main__':
    test_assignments = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]
    assert (len(filter_assignment_pairs(test_assignments, contains)) == 2)
    assert (len(filter_assignment_pairs(test_assignments, overlap)) == 4)

    with open(join(dirname(__file__), "input"), "r") as f:
        assignment_pairs = [line[:-1] for line in f.readlines()]
        redundant = len(filter_assignment_pairs(assignment_pairs, contains))
        overlapping = len(filter_assignment_pairs(assignment_pairs, overlap))

        print(
            f"[Day 4] Redundant assignments (1st part): {redundant}, "
            f"Overlapping assignments (2st part): {overlapping}"
        )
