from os.path import join, dirname


def item_priority(item):
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    if 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27


def take_redundant(rucksack):
    n = len(rucksack) // 2
    return (set(rucksack[:n]) & set(rucksack[n:])).pop()


def redundant_item_priorities(rucksacks):
    return [item_priority(take_redundant(rucksack)) for rucksack in rucksacks]


def find_group_badge(rucksacks):
    return (set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])).pop()


def group_item_priorities(rucksacks):
    return [item_priority(find_group_badge(rucksacks[i:i+3])) for i in range(0, len(rucksacks), 3)]


if __name__ == '__main__':
    test_rucksacks = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    assert (sum(redundant_item_priorities(test_rucksacks)) == 157)
    assert (sum(group_item_priorities(test_rucksacks)) == 70)

    with open(join(dirname(__file__), "input"), "r") as f:
        rucksacks = [line[:-1] for line in f.readlines()]
        redundant_item_priorities = sum(redundant_item_priorities(rucksacks))
        group_item_priorities = sum(group_item_priorities(rucksacks))
        print(
            f"Sum of priorities (1st part): {redundant_item_priorities}, "
            f"Sum of priorities (2nd part): {group_item_priorities}"
        )
