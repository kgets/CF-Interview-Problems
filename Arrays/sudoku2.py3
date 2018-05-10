def isDuplicates(List):
    s=set()
    for e in List:
        if e!='.':
            if e in s:
                return 1
            s.add(e)
    return 0
    
def sudoku2(grid):
    #check row
    for r in grid:
        if isDuplicates(r):
            return 0
    #check column
    for c in zip(*grid):
        if isDuplicates(c):
            return 0
    #check squares
    for y in range(3):
        for x in range(3):
            if isDuplicates(grid[y*3][x*3:x*3+3]+grid[y*3+1][x*3:x*3+3]+grid[y*3+2][x*3:x*3+3]):
                return 0
    return 1
