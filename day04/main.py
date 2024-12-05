DIRECTIONS = [
  (-1,  0), #North
  (-1,  1), #Northeast
  (0,   1), #East
  (1,   1), #Southeast
  (1,   0), #South
  (1,   -1), #Southwest
  (0,   -1), #West
  (-1,  -1), #NorthWest
]

def read_lines(path):
  lines = None
  with open(path) as file:
      lines = [line.rstrip() for line in file]
  return lines

def read_grid(path):
  lines = read_lines(path)
  rows = len(lines)
  cols = len(lines[0])
  for i in range(rows):
    assert len(lines[i]) == cols
  print(f'read grid at {path}:: rows:{rows}  cols:{cols}')
  return (lines, rows, cols)


def find_words_in_grid(word, grid):
  rows = len(grid)
  cols = len(grid[0])

  def gridchar(r,c):
    '''return char at pos (or - if out of range)'''
    try: 
      ch = grid[r][c]
    except:
      ch = '-'
    return ch

  def word_found(r, c, dr, dc):
    """
    does the word exist in the grid at the given location in the given direction
    """
    for i in range(len(word)):
      cr = r + i * dr #currrent row
      cc = c + i * dc #current col
      # print(f'startpos:({r},{c},{gridchar(r,c)})\t curpos:({cr},{cc},{gridchar(cr,cc)})\t word[i]:{word[i]}')
      if cr < 0 or cr >= rows:
        return False
      if cc < 0 or cc >= cols:
        return False
      if word[i] != grid[cr][cc]:
        return False
    print(f'word found at ({r},{c}) in direction ({dr}, {dc})')
    return True
  
  findcount = 0

  for direction in DIRECTIONS:  
    dr, dc = direction
    for i in range(rows):
      for j in range(cols):
        if word_found(i, j, dr, dc):
          findcount += 1
  
  print(f'total occurrences: {findcount}')
  return findcount


def main_part1(path):
  grid, rows, cols = read_grid(path)
  find_words_in_grid('XMAS', grid)
  

def main_part2(path):
  pass
   


def main():
  main_part1('resources/sample.txt')
  main_part1('resources/input.txt')

  # main_part2('resources/sample.txt')
  # main_part2('resources/input.txt')


if __name__ == "__main__":
  main()
