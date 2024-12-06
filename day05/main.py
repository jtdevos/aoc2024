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


def is_valid_pageorder(rule, pageorder):
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
  is_valid = not(lpageIdx > -1 and rpageIdx > -1 and lpageIdx > rpageIdx)
  return is_valid



def check_rules(rules, pageOrderings):
  validUpdates = []
  for pageOrdering in pageOrderings:
    if any(not is_valid_pageorder(rule, pageOrdering) for rule in rules):
      print(f'page order not valid: {pageOrdering}')
    else: 
      validUpdates.append(pageOrdering)
  return validUpdates
    

    # for rule in rules:    
    #   if is_valid_pageorder(rule, pageOrdering):
    #     print(f'rule {rule} is valid for: {pageOrdering}')
    

         


def main():
  print(f'hello from main')
  line_sections = parse_sections('resources/sample.txt');
  rules, pageOrderings = line_sections
  for s in line_sections:
    print(f'section: {s}')

  validUpdates = check_rules(rules, pageOrderings)
  print(f'valid updates: {validUpdates}')
  for update in validUpdates:
    idx = int((len(update)-1)/2)
    print(f'middle index: {update[idx]}')


if __name__ == "__main__":
   main()