def read_lines(path):
    lines = None
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines


def getnumlists(filepath):
    lines = read_lines(filepath)
    split_lines = [line.split(" ") for line in lines]
    left_nums = sorted([int(v[0]) for v in [line.split(" ") for line in lines]])
    right_nums = sorted([int(v[-1]) for v in [line.split(" ") for line in lines]])
    return left_nums, right_nums


def comparenums(filepath):
    lines = read_lines(filepath)
    split_lines = [line.split(" ") for line in lines]
    left_nums = sorted([int(v[0]) for v in [line.split(" ") for line in lines]])
    right_nums = sorted([int(v[-1]) for v in [line.split(" ") for line in lines]])

    numpairs = [(left_nums[i], right_nums[i]) for i, x in enumerate(left_nums)]
    #  numpairs = [(int(v[0]),int(v[-1])) for v in [line.split(' ') for line in lines]]
    difpairs = [abs(v[0] - v[1]) for v in numpairs]
    #  left_nums = [int(v[0]) for v in split_lines]
    print("opened file")
    print(f"lines: {split_lines}")
    print(f"left_nums: {left_nums}")
    print(f"right_nums: {right_nums}")
    print(f"numpairs: {numpairs}")
    print(f"difpairs: {difpairs}")
    print(f" sum of difpairs: {sum(difpairs)}")


def count_occurrences(n, vals):
    ncount = vals.count(n)
    return ncount


def calcsimscores(filepath):
    left_nums, right_nums = getnumlists(filepath)
    scoresum = 0

    for n in left_nums:
        ncount = count_occurrences(n, right_nums)
        sscore = n * ncount
        # print(f'maches of {n} in {right_nums}: {ncount}')
        print(f"similarity score of ({n}, {ncount}): {sscore}")
        scoresum = scoresum + sscore
    print(f"scoresum: {scoresum}")


def main():
    print("hello from main")
    comparenums("resources/sample.txt")
    comparenums("resources/input.txt")


def main2():
    calcsimscores("resources/sample.txt")
    calcsimscores("resources/input.txt")


# main()

main2()
