from os.path import join, dirname


def heavier_bag_weight(bags):
    return max([sum(bag) for bag in bags])


def heavier_bags_weight(bags, n=3):
    return sum(sorted([sum(bag) for bag in bags], reverse=True)[:n])


def make_bags(lines):
    res, bag = [], []
    for item in lines:
        if item == '' or item == '\n':
            res.append(bag)
            bag = []
        else:
            bag.append(int(item))
    return res


if __name__ == '__main__':
    test_bags = [[1000, 2000, 3000], [4000], [
        5000, 6000], [7000, 8000, 9000], [10000]]
    assert (heavier_bag_weight(test_bags) == 24000)
    assert (heavier_bags_weight(test_bags) == 45000)

    with open(join(dirname(__file__), "input"), "r") as f:
        bags = make_bags(f.readlines())
        print(f"Heaviest bag: {heavier_bag_weight(bags)}, "
              f"top 3: {heavier_bags_weight(bags, 3)}")
