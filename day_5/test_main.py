from main import CrateStacks
import pytest

INPUT = ["    [D]    ",
         "[N] [C]    ",
         "[Z] [M] [P]",
         " 1   2   3 "]

INPUT_PROCEDURE = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

def test_crate_init():
    cs = CrateStacks(INPUT)
    assert len(cs.get_piles()) == 3
    cs = CrateStacks([INPUT[-1]])
    assert len(cs.get_piles()) == 3

def test_crate_top():
    cs = CrateStacks(INPUT)
    assert cs.top("1") == "N" 
    assert cs.top("2") == "D" 
    assert cs.top("3") == "P"

    cs = CrateStacks([INPUT[-1]])
    assert cs.top("1") == None
    assert cs.top("2") == None
    assert cs.top("3") == None

def test_crate_pop():
    cs = CrateStacks(INPUT)
    assert cs.pop("1") == "N"
    assert cs.top("1") == "Z"  
    assert cs.pop("1") == "Z"
    assert cs.top("1") == None

    assert cs.pop("2", 2) == ["D", "C"]
    assert cs.top("2") == "M"

def test_crate_move():
    cs = CrateStacks(INPUT)
    h1 = cs.get_height("1")
    h3 = cs.get_height("3")
    cs.move(2, "1", "3")
    assert cs.get_height("1") == h1 - 2
    assert cs.get_height("3") == h3 + 2
    assert cs.top("3", 2) == ["Z", "N"]

def test_example():
    cs = CrateStacks(INPUT_PROCEDURE)
    assert(cs.get_tops() == "CMZ")