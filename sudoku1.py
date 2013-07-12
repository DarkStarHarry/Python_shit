import math
class Sudoku:
    def __init__(self, p):
        self.p = p
        self.sqrSz = int(math.sqrt(len(p)))
        
    def solve(self):
        return self.solveCell(0, 0)
    
    def solveCell(self, row, col):
        if col >= len(self.p):
            return True
        elif row >= len(self.p):
            return self.solveCell(0, col+1)
        elif self.p[row][col] != 0:
            return self.solveCell(row+1, col)
        for num in range(1,len(p)+1):
            if (self.valid(row, col, num)):
                self.p[row][col] = num
                if self.solveCell(row+1, col):
                    return True
        self.p[row][col]=0
        return False

    def validInRow(self, row, num):
        for col in range(len(self.p)):
            if abs(self.p[row][col]) == num:
                return False 
        return True

    def validInCol(self, col, num):
        for row in range(len(self.p)):
            if abs(self.p[row][col]) == num:
                return False 
        return True
    def validInSquare(self, row, col, num):
        r1 = int(row / self.sqrSz) * self.sqrSz
        c1 = int(col / self.sqrSz) * self.sqrSz
        for r in range(r1, (r1+self.sqrSz)):
            for c in range(c1, (c1+self.sqrSz)):
                if abs(self.p[r][c]) == num:
                    return False 
        return True

    def valid(self, row, col, num):
        isValid = self.validInRow(row, num) and self.validInCol(col, num) and self.validInSquare(row, col, num)
        return isValid

    def put(self):
        for row in range(len(self.p)):
            for col in range(len(self.p)):
                print '%-2d' % abs(self.p[row][col]),

p = [
    [-7, 0, 0, -6, -3, -2, 0, 0, 0],
    [0, 0, 0, 0, -8, -1, 0, 0, -9],
    [-1, -3, -4, 0, 0, 0, 0, 0, -2],
    [0, 0, 0, -8, 0, -4, 0, -2, 0],
    [0, -2, 0, 0, -1, 0, 0, -5, 0],
    [0, -7, 0, -3, 0, -5, 0, 0, 0],
    [-2, 0, 0, 0, 0, 0, -6, -7, -8],
    [-3, 0, 0, -1, -5, 0, 0, 0, 0],
    [0, 0, 0, -2, -7, -8, 0, 0, -5]]

s = Sudoku(p)
print "Unsolved:"
s.put()
if s.solve():
    print "Solved:"
    s.put()
else:
    print "Puzzle has no solution"
    s.put()
