import re

REX_MUL = re.compile(r'(mul)\((\d{1,3}),(\d{1,3})\)')

def read_lines(path):
  lines = None
  with open(path) as file:
      lines = [line.rstrip() for line in file]
  return lines



def read_commands(path):
  lines = read_lines(path)
  allcmds = []
  for line in lines:
    cmds = REX_MUL.findall(line)
    print(f'found {len(cmds)} commands: {cmds}')
    #make sure all commands have 3 terms
    assert(all(len(cmd)==3 for cmd in cmds))
    allcmds += cmds
  return  allcmds
      

def process_muls(cmds):
  """execute each multiplication, and add the products to a sum"""

  total = 0
  for cmdname, lterm, rterm in cmds:
    lterm = int(lterm)
    rterm = int(rterm)
    print(cmdname, lterm, rterm, lterm*rterm)
    total += (lterm * rterm)
  print(f'sum of products: {total}')


def main():
  # cmds = read_commands('resources/sample.txt')
  # process_muls(cmds)
  cmds = read_commands('resources/input.txt')
  process_muls(cmds)





if __name__ == "__main__":
  main()
