class Board:
    def _init_(self, size=8):
        self.size = size

        self.grid = [[Cell for _ in range(8)] for _ in range(8)]
        self.initialize_board()
        Cell()

    def initialize_board(self):
        

# Place les 4 pions de départ
        self.grid[3][3] = Pawn('O')
        self.grid[3][4] = Pawn('*')
        self.grid[4][3] = Pawn('*')
        self.grid[4][4] = Pawn('O')
    
def display(self):
    for row in self.grid:
        row_display = " "
        for cell in row: 
            if cell is None:
                row_display += "*"
            else:
                row_display += f"{cell}"
                print(row_display.strip())
            print()

def place_Pawn(self, x, y, Pawn):
    if 0 <= x < self.size and 0 <= y < self.size:
        if self.grid [y][x]is None:
            


        
        