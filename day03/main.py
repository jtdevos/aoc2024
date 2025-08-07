import re

REX_MUL = re.compile(r"(mul)\((\d{1,3}),(\d{1,3})\)")
REX_CONDMUL = re.compile(r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")


def read_lines(path):
    lines = None
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines


def read_commands(path, pattern=REX_MUL):
    lines = read_lines(path)
    allcmds = []
    for line in lines:
        cmds = pattern.findall(line)
        # print(f'found {len(cmds)} commands')
        # make sure all commands have 3 terms
        # assert(all(len(cmd)==3 for cmd in cmds))
        allcmds += cmds
    return allcmds


def process_muls(cmds):
    """execute each multiplication, and add the products to a sum"""

    total = 0
    for cmdname, lterm, rterm in cmds:
        lterm = int(lterm)
        rterm = int(rterm)
        # print(cmdname, lterm, rterm, lterm*rterm)
        total += lterm * rterm
    print(f"star one total: {total}")


def process_conds(cmds):
    enabled = True
    total = 0
    for cmd in cmds:
        cmdname, lterm, rterm, isdo, isdont = cmd
        if cmd[3]:
            # print("do")
            enabled = True
        if cmd[4]:
            # print("DONT")
            enabled = False
        if cmdname and enabled:
            lterm = int(lterm)
            rterm = int(rterm)
            total += lterm * rterm
    return total


def main_part1():
    # cmds = read_commands('resources/sample.txt')
    # process_muls(cmds)
    cmds = read_commands("resources/input.txt")
    process_muls(cmds)


def main_part2(path):
    cmds = read_commands(path, REX_CONDMUL)
    total = process_conds(cmds)
    print(f"star two total: {total}")


def main():
    main_part1()
    main_part2("resources/input.txt")


if __name__ == "__main__":
    main()
