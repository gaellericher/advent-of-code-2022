from os.path import join, dirname
import re


def is_visible(forest, i, j):
    # Trees on the outside of the forest are visible from outside
    if i == 0 or i == len(forest) - 1 or\
            j == 0 or j == len(forest[0]) - 1:
        return True

    h = forest[i][j]

    # Is it visible from the left or right?
    if max(forest[i][:j]) < h or max(forest[i][j+1:]) < h:
        return True

    # Is it visible from the top or bottom?
    col = [forest[k][j] for k in range(0, len(forest[0]))]
    if max(col[:i]) < h or max(col[i+1:]) < h:
        return True

    return False

def view_span(arr, h):
    for i, v in enumerate(arr):
        if v >= h:
            return i+1 
    return len(arr)

def tree_scenic_score(forest, i, j):
    h = forest[i][j]

    # Look left and right
    left_dist = view_span(forest[i][:j][::-1], h)
    right_dist = view_span(forest[i][j+1:], h)
    
    # Look top and bottom
    col = [forest[k][j] for k in range(0, len(forest[0]))]
    top_dist = view_span(col[:i][::-1], h)
    bottom_dist = view_span(col[i+1:], h)

    return left_dist*right_dist*top_dist*bottom_dist


def count_visible_from_outside(forest):
    count = 0
    for i in range(0, len(forest)):
        for j in range(0, len(forest[0])):
            if is_visible(forest, i, j):
                count += 1
    return count

def highest_scenic_score(forest):
    best_score = 0
    for i in range(0, len(forest)):
        for j in range(0, len(forest[0])):
            tree_score = tree_scenic_score(forest, i, j)
            best_score = max(best_score, tree_score)
    return best_score


if __name__ == '__main__':
    with open(join(dirname(__file__), "input"), "r") as f:
        forest = [line[:-1] for line in f.readlines()]
        print(
            f"[Day 5] Visible from outside (1st part): {count_visible_from_outside(forest)}, "
            f"Highest scenic score possible (2st part): {highest_scenic_score(forest)}"
        )
