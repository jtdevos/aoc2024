import os

def read_lines(path):
  lines = None
  with open(path) as file:
      lines = [line.rstrip() for line in file]
  return lines



def read_line_sections(path, delim=os.linesep):
  """return list of line sections, delimited by single newline"""
  lines = None
  sections = []
  section = []
  with open(path) as file:
    for line in file:
      if line == delim:
        sections.append(section)
        section = []
      else:
        section.append(line.rstrip())
  # don't forget to tack on the last line
  sections.append(section)
  return sections

def parse_sections(path):
  """convert sections of lines into lists of numbers. return the 2 parsed sections"""
  sections = read_line_sections(path)
  assert len(sections) == 2
  s0 = [[int(x) for x in line.split('|')] for line in sections[0]]
  s1 = [[int(x) for x in line.split(',')] for line in sections[1]]
  sections = [s0, s1]
  return sections

def process_rule(rule, pageorder):
  lpage, rpage = rule
  lpageIdx = -1
  rpageIdx = -1
  validOrdering = True
  for idx, pagenum in enumerate(pageorder):
    # print(f'lpage:{lpage} rpage:{rpage} pagenum:{pagenum}')
    if lpage == pagenum and lpageIdx<0:
      lpageIdx = idx
    if rpage == pagenum and rpageIdx<0:
      rpageIdx = idx
    if rpageIdx>-1 and lpageIdx>-1:
      break
  return lpageIdx, rpageIdx

def is_valid_pageorder(rule, pageorder):
  lpage, rpage = rule
  lpageIdx, rpageIdx = process_rule(rule, pageorder)
  is_valid = not(lpageIdx > -1 and rpageIdx > -1 and lpageIdx > rpageIdx)
  return is_valid

def check_rules(rules, pageOrderings):
  validUpdates = []
  invalidUpdates = []
  for pageOrdering in pageOrderings:
    if any(not is_valid_pageorder(rule, pageOrdering) for rule in rules):
      # print(f'page order not valid: {pageOrdering}')
      invalidUpdates.append(pageOrdering)
    else:
      validUpdates.append(pageOrdering)
  return validUpdates, invalidUpdates


def part1(path):
  line_sections = parse_sections(path);
  rules, pageOrderings = line_sections
  for s in line_sections:
    print(f'section: {s}')

  validUpdates, ignored = check_rules(rules, pageOrderings)
  print(f'valid updates: {validUpdates}')
  total = 0
  for update in validUpdates:
    idx = int((len(update)-1)/2)
    midnum = update[idx]
    total += midnum
    print(f'middle index: {update[idx]}')
  print(f'total of middles: {total}')

def part2(path):
  line_sections = parse_sections(path)
  rules, pageUpdates = line_sections
  ignored, invalidUpdates = check_rules(rules, pageUpdates)
  assert(len(pageUpdates) == len(ignored) + len(invalidUpdates))
  fixedUpdates = []
  for update in invalidUpdates:
    print(f'invalid update: {update}')
    # now get all the violating rules for this update
    brokenrules = [rule for rule in rules if not is_valid_pageorder(rule, update)]
    fixedupdate = update[:]
    for br in brokenrules:
      # fixing one broken rule might implicitly fix others, recheck 
      if  is_valid_pageorder(br, fixedupdate):
        print(f'rule {br} no longer broken by {fixedupdate}')
      else:
        print(f'broken rule: {br}, orig update:{fixedupdate}')
        lpage, rpage = br
        lidx, ridx = process_rule(br, fixedupdate)
        page = fixedupdate.pop(ridx)
        assert(rpage == page)
        print(f'   removed {page}: new update:{fixedupdate}')
        fixedupdate.insert(lidx, rpage)
        print(f'   current update: {fixedupdate}')
    print(f'update:{update} becomes {fixedupdate}')
    fixedUpdates.append(fixedupdate)
  total = 0
  assert(len(fixedUpdates) == len(invalidUpdates))
  for update in fixedUpdates:
    idx = int((len(update)-1)/2)
    midnum = update[idx]
    total += midnum
    print(f'midnum of {update} is {midnum}')
  print(f'total of midnums is: {total}')
      





def main():
    # part1('resources/sample.txt')
    part1('resources/input.txt')
    # part2('resources/sample.txt')
    part2('resources/input.txt')

if __name__ == "__main__":
   main()
