class Board:
    def __init__(self):
        self.board = [["E","E","E"],["E","E","E"],["E","E","E"]]
    def printBoard(self):
        rowIdArray = ["A","B","C"]
        colId = "  1   2   3"
        print(colId)
        rowId = 0
        for row in self.board:
            line = ""
            line += rowIdArray[rowId] + " "
            for col in row:
                line += col + " | "
            #Remove the last 3 characters from the line
            line = line[:-3]
            print(line)
            rowId += 1
            
    def setBoard(self, board):
        self.board = board
    def getBoard(self):
        return self.board
    def setCell(self, row, col, value):
        self.board[row][col] = value
    def getCell(self, row, col):
        return self.board[row][col]
    def checkWinner(self):
        #Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != "E":
                return row[0]
        #Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != "E":
                return self.board[0][i]
        #Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "E":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "E":
            return self.board[0][2]
        
        #Check for tie
        tie = True
        for row in self.board:
            for col in row:
                if col == "E":
                    tie = False
        if tie:
            return "T"
        return "E"
    
