from main import find_marker
import pytest

INPUT_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
INPUT_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
INPUT_3 = "nppdvjthqldpwncqszvftbrmjlhg"
INPUT_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
INPUT_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def test_find_paquet_marker():
    assert(find_marker("", marker_size=4) == None)
    assert(find_marker("mjqf", marker_size=4) == 4)
    assert(find_marker("mjqjka", marker_size=4) == 6)
    assert(find_marker(INPUT_1, marker_size=4) == 7)
    assert(find_marker(INPUT_2, marker_size=4) == 5)
    assert(find_marker(INPUT_3, marker_size=4) == 6)
    assert(find_marker(INPUT_4, marker_size=4) == 10)
    assert(find_marker(INPUT_5, marker_size=4) == 11)

def test_find_message_marker():
    assert(find_marker("", marker_size=14) == None)
    assert(find_marker("mjqf", marker_size=14) == None)
    assert(find_marker("mjqjka", marker_size=14) == None)
    assert(find_marker(INPUT_1, marker_size=14) == 19)
    assert(find_marker(INPUT_2, marker_size=14) == 23)
    assert(find_marker(INPUT_3, marker_size=14) == 23)
    assert(find_marker(INPUT_4, marker_size=14) == 29)
    assert(find_marker(INPUT_5, marker_size=14) == 26)