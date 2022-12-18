from main import build_filesystem
import pytest

INPUT = ["$ cd /",
         "$ ls",
         "dir a",
         "14848514 b.txt",
         "8504156 c.dat",
         "dir d",
         "$ cd a",
         "$ ls",
         "dir e",
         "29116 f",
         "2557 g",
         "62596 h.lst",
         "$ cd e",
         "$ ls",
         "584 i",
         "$ cd ..",
         "$ cd ..",
         "$ cd d",
         "$ ls",
         "4060174 j",
         "8033020 d.log",
         "5626152 d.ext",
         "7214296 k"
         ]



def test_init():
    root = build_filesystem(["$ cd /"])
    assert(root.to_string() == "- / (dir)")
    root = build_filesystem(INPUT)
    a = root.get_child_by_name("a")
    assert(a.size() == 94853)
    assert(a.get_child_by_name("e").size() == 584)
    d = root.get_child_by_name("d")
    assert(d.size() == 24933642)
    assert(d.to_string().split("\n")[-1] == " - k (file, size=7214296)")
    assert(root.size() == 48381165)

def test_smaller_than():
    root = build_filesystem(INPUT)
    smallest_dir = root.find_directories(lambda d: d.size() <= 100000)
    assert([d.name for d in smallest_dir] == ["a", "e"])
    assert(sum([d.size() for d in smallest_dir]) == 95437)
    