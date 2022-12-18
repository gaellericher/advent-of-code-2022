from os.path import join, dirname
import re

CRANE_9000 = "CrateMover 9000"
CRANE_9001 = "CrateMover 9001"

class CrateStacks:
    piles = dict()  # Stacks are list with top at the end
    crane = None

    def __init__(self, input_lines, crane = CRANE_9000):
        try:
            split_idx = input_lines.index("")
            init_stacks, procedure = input_lines[:split_idx], input_lines[split_idx+1:]
        except:
            init_stacks, procedure = input_lines, []
        self.crane = crane
        self.parse_init_stacks(rows=init_stacks[:-1], names=init_stacks[-1])
        self.apply_procedure(procedure)

    def top(self, pile, n=1):
        l = len(self.piles[str(pile)])
        if n > l:
            return None
        top_n = self.piles[str(pile)][-n:]
        return top_n[-1] if n == 1 else top_n[::-1]

    def pop(self, pile, n=1):
        top_n = self.top(pile, n)
        if top_n is not None:
            self.piles[str(pile)] = self.piles[str(pile)][:-n]
        return top_n

    def drop(self, pile, crates):
        if crates is None:
            return
        if isinstance(crates, list):
            if self.crane == CRANE_9000:
                self.piles[str(pile)].extend(crates)
            elif self.crane == CRANE_9001:
                self.piles[str(pile)].extend(crates[::-1])
        elif crates != ' ' and crates != " ":
            self.piles[str(pile)].append(crates)

    def parse_init_stacks(self, rows, names):
        names = re.findall(r"\s(\d+)\s", names)
        self.piles = {k: [] for k in names}
        for row in rows[::-1]:
            for pile, crate in enumerate(row[1::4]):
                self.drop(f"{pile+1}", crate)

    def to_string(self):
        res = []
        tallest_pile = max(self.get_height(pile) for pile in self.get_piles())
        for i in range(tallest_pile, -1, -1):
            row = " ".join([str(f"[{pile[i]}]" if i < len(
                pile) else "   ") for pile in self.piles.values()])
            res.append(row)
        res.append(" " + "   ".join(self.get_piles()) + " ")
        return "\n".join(res)

    def get_piles(self):
        return self.piles.keys()

    def move(self, n, from_pile, to_pile):
        self.drop(to_pile, self.pop(from_pile, n))

    def get_height(self, pile):
        return len(self.piles[str(pile)])

    def apply_procedure(self, procedure):
        for instruction in procedure:
            instruction = re.findall(r"([a-z]+)\s(\d+)\sfrom\s(\d+)\sto\s(\d+)", instruction)
            if len(instruction) > 0 and instruction[0][0] == "move":
                op, n, from_pile, to_pile = instruction[0]
                self.move(int(n), from_pile, to_pile)

    def get_tops(self):
        return "".join([self.top(pile) for pile in self.get_piles()])

if __name__ == '__main__':
    with open(join(dirname(__file__), "input"), "r") as f:
        full_input = [line[:-1] for line in f.readlines()]
        crane9000 = CrateStacks(full_input, crane = CRANE_9000)
        crane9001 = CrateStacks(full_input, crane = CRANE_9001)
        print(
            f"[Day 5] Top of stacks (1st part): {crane9000.get_tops()}, "
            f"Top of stacks (2st part): {crane9001.get_tops()}"
        )
