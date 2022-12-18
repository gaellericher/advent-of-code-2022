from os.path import join, dirname


def score_shape(shape):
    """
        Return 1 for Rock (A or X), 2 for Paper (B or Y), etc
    """
    if 'A' <= shape <= 'C':
        return ord(shape) - ord('A') + 1
    if 'X' <= shape <= 'Z':
        return ord(shape) - ord('X') + 1
    return 0


def score_round_1(theirs, ours):
    """
        Return 0 if our shape loses, 3 if the round is a draw, and 6 if our shape wins, plus our shape score
    """
    score = score_shape(ours)
    if score_shape(theirs) == score_shape(ours):
        score += 3
    elif (score_shape(theirs) % 3) == score_shape(ours) - 1:
        score += 6
    return score


def score_round_2(theirs, outcome):
    """
        Return 0 if we need to lose, 3 if we need to draw, and 6 if we need to win, plus our shape score
    """
    if outcome == "X":
        return (score_shape(theirs) - 2) % 3 + 1
    elif outcome == "Y":
        return score_shape(theirs) + 3
    else:  # Z
        return score_shape(theirs) % 3 + 1 + 6


def score_rounds(rounds, round_scoring_fun):
    return [round_scoring_fun(theirs, ours) for (theirs, ours) in rounds]


def total_score(rounds, round_scoring_fun):
    return sum(score_rounds(rounds, round_scoring_fun))


if __name__ == '__main__':
    test_rounds = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
    assert (total_score(test_rounds, score_round_1) == 8+1+6)
    test_rounds = [('C', 'X'), ('A', 'Z'), ('C', 'Y')]
    assert (total_score(test_rounds, score_round_1) == 7+3+2)

    test_rounds = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
    assert (total_score(test_rounds, score_round_2) == 4+1+7)
    test_rounds = [('C', 'X'), ('A', 'Z'), ('C', 'Y')]
    assert (total_score(test_rounds, score_round_2) == 2+8+6)

    with open(join(dirname(__file__), "input"), "r") as f:
        rounds = [tuple(line.split()) for line in f.readlines()]
        print(f"[Day 2] Total score (1st part): {total_score(rounds, score_round_1)}, "
              f"Total score (2st part): {total_score(rounds, score_round_2)}"
              )
