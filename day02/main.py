def read_lines(path):
  lines = None
  with open(path) as file:
      lines = [line.rstrip() for line in file]
  return lines


def read_nums(path):
  lines = read_lines(path)
  splitlines = [line.split(' ') for line in lines]
  numlines = [[int(x) for x in line ] for line in splitlines]
  return numlines



def report_pairs(report):
  pairs = [(report[i], report[i+1]) for i in range(len(report)-1)]
  return pairs


def all_increasing(levels):  
  pairs = report_pairs(levels)
  return all(p[0] < p[1] for p in pairs)

def all_decreasing(levels):  
  pairs = report_pairs(levels)
  return all(p[0] > p[1] for p in pairs)

def all_gradual(levels, dmin, dmax):
  pairs = report_pairs(levels)
  outval = True
  for p in pairs:
    d = abs(p[0] - p[1])
    if d < dmin or d > dmax:
      outval = False
      break
  return outval

def count_passing_reports(filepath):
  reports  = read_nums(filepath)
  passcount = 0
  for rpt in reports:
    incOrDec = all_increasing(rpt) or all_decreasing(rpt)
    grad = all_gradual(rpt, 1, 3)
    print(f'rpt:{rpt}\t inc:{all_increasing(rpt)}\t dec:{all_decreasing(rpt)}\t incOrDec:{incOrDec}\t grad:{grad}')
    if incOrDec and grad:
      passcount += 1  

  print(f'passcount for {filepath}: {passcount}')
  return passcount




def main():
  print("in main")
  numlines = read_nums('resources/sample.txt')
  print(f'numlines: {numlines}')
  # for i, rpt in enumerate(numlines):
  #   allgrad = all_gradual(rpt, 1, 3)
  #   print(f'pairs for line {i}: {rpt}, all_increasing:{all_increasing(rpt)}, all_decreasing:{all_decreasing(rpt)}, allgrad: {allgrad}')

  pcsample = count_passing_reports('resources/sample.txt')
  pcinput = count_passing_reports('resources/input.txt')
if __name__ == "__main__":
  main()
