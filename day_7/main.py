from os.path import join, dirname
import re


class Directory:
    name = None
    parent = None
    children = None
    files = None

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def add_child(self, child):
        self.children.append(child)
    
    def add_file(self, f):
        self.files.append(f)

    def to_string(self, indent=0):
        res = [f"{''.join([' ']*indent)}- {self.name} (dir)"]
        for d in self.children:
            res.append(d.to_string(indent=indent+1))
        for f in self.files:
            res.append(f.to_string(indent=indent+1))
        return "\n".join(res)

    def size(self):
        res = sum([f.size for f in self.files])
        for d in self.children:
            res += d.size()
        return res

    def get_child_by_name(self, name):
        return next(filter(lambda child: child.name == name, self.children), None)
    
    def get_path_to_root(self):
        if self.name == "/":
            return self.name
        res = [self.name]
        parent = self.parent
        while parent is not None:
            res.append(parent.name)
            parent = parent.parent
        return "/".join(res[::-1])[1:]

    def find_directories(self, predicate):
        res = []
        if predicate(self):
            res.append(self)
        for d in self.children:
            res.extend(d.find_directories(predicate))
        return res

class File:
    size = 0
    name = None
    parent = None

    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = int(size)
        self.parent = parent
    
    def to_string(self, indent=0):
        return f"{''.join([' ']*indent)}- {self.name} (file, size={self.size})"


def get_command_result(history):
    res = []
    for line in history:
        if line.startswith('$'):
            return res
        else:
            res.append(line)
    return res

def build_filesystem(history):
    root = Directory("/")
    cur_dir = None
    for i, line in enumerate(history):
        if line.startswith('$'):
            command = re.findall(r"\$\s([a-z]+)\s?([a-zA-Z1-9\/\.]+)?$", line)
            (op, param), result = command[0], get_command_result(history[i+1:])
            i += len(result)
            if op == "cd":
                if param == "..":
                    cur_dir = cur_dir.parent
                elif param == "/":
                    cur_dir = root
                elif len(param) > 0:
                    cur_dir = cur_dir.get_child_by_name(param)
            elif op == "ls":
                for element in result:
                    dir_or_size, name = element.split()
                    if dir_or_size == "dir":
                        new_dir = Directory(name=name, parent=cur_dir)
                        cur_dir.add_child(new_dir)
                    else:
                        cur_dir.add_file(File(name=name, size=dir_or_size))
    return root      


if __name__ == '__main__':
    total_available_disk_space = 70000000
    required_disk_space = 30000000
    

    with open(join(dirname(__file__), "input"), "r") as f:
        history = [line[:-1] for line in f.readlines()]
        root = build_filesystem(history)

        # 1st part
        smallest_under_10000 = root.find_directories(lambda d: d.size() <= 100000)
        sum_sizes = sum([d.size() for d in smallest_under_10000])

        #2nd part
        needed_space = required_disk_space - total_available_disk_space + root.size()
        smallest_above_needed_space = root.find_directories(lambda d: d.size() >= needed_space)
        min_sizes = min([d.size() for d in smallest_above_needed_space])

        print(
            f"[Day 7] Sum of small directory sizes (1st part): {sum_sizes}, "
            f"Minimum size of directory to delete (2st part): {min_sizes}"
        )
