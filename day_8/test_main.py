from main import count_visible_from_outside, highest_scenic_score, tree_scenic_score
import pytest

INPUT = ["30373",
         "25512",
         "65332",
         "33549",
         "35390"]


def test_count_visible_from_outside():
    assert(count_visible_from_outside(INPUT) == 21)

def test_highest_scenic_score():
    assert(tree_scenic_score(INPUT, 1, 2) == 4)
    assert(highest_scenic_score(INPUT) == 8)

