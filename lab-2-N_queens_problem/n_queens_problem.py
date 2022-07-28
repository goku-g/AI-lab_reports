import pprint

class grid:
    def __init__(self, nfquen:int):
        self.queens = nfquen
        self.grid = [[' ' for i in range(self.queens)] for j in range(self.queens)]
    

    def is_safe(self, posx, posy):
        for row in range(self.queens):
            if(self.grid[row][posy] == 'Q'):
                return False
        for col in range(self.queens):
            if(self.grid[posx][col] == 'Q'):
                return False
        
        
        row = posx
        col = posy
        while(row>=0 and col>=0):
            if(self.grid[row][col] == 'Q'):
                return False
            row -= 1
            col -= 1
        row = posx
        col = posy
        while(row<self.queens and col<self.queens):
            # print(row, col, end=",")
            if(self.grid[row][col] == 'Q'):
                return False
            row += 1
            col += 1
        row = posx
        col = posy
        while(row<self.queens and col>=0):
            # print(row, col, end=",")
            if(self.grid[row][col] == 'Q'):
                return False
            row += 1
            col -= 1
        row = posx
        col = posy
        while(row>=0 and col<self.queens):
            # print(row, col)
            if(self.grid[row][col] == 'Q'):
                return False
            row -= 1
            col += 1

        return True
    
    def palce_queen(self, posx, posy):
        self.grid[posx][posy] = 'Q'

    def reset(self, posx, posy):
        # self.grid = [[' ' for i in range(self.queens)] for j in range(self.queens)]
        self.grid[posx][posy] = ' '

    def show(self):
        pprint.pprint(self.grid)

def nqueen(board, index, queens):
    if(index >= queens):
        return True

    for col in range(queens):
        if(board.is_safe(index, col)):
            board.palce_queen(index, col)
            if(nqueen(board, index+1, queens)):
                return True
            board.reset(index, col)
    return False

nfqueen = int(input("Enter no. of Queen: "))
board = grid(nfqueen)

done = nqueen(board, 0, nfqueen)


if(done):
    board.show()
else:
    print("No solution!")