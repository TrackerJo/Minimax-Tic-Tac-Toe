from board import Board
from minimax import findBestMove


def main():
    currentBoard = Board()
    
    run = True
    turn = 1 
    while run:
        takeTurn(turn, currentBoard)

       
        print("\n")
        winner = currentBoard.checkWinner()
        if winner != "E" and winner != "T":
            print("The winner is " + winner)
            run = False
        elif winner == "T":
            print("Tie Game")
            run = False

        turn = (turn + 1) % 2

def takeTurn(turn, currentBoard):
    if turn == 0:
        print("AI's turn")
        bestMove = findBestMove(currentBoard.getBoard())
        
        row = bestMove[0]
        col = bestMove[1]
    else:
        rowIdArray = ["A","B","C"]
        print("Your turn")
        currentBoard.printBoard()
        cell = input("Enter the cell (e.x A1): ")
        row = rowIdArray.index(cell[0])
        col = int(cell[1]) - 1
    
    
    

   
    if currentBoard.getCell(int(row), col) == "E":
        if turn == 0:
            currentBoard.setCell(int(row), col, "X")
        else:
            currentBoard.setCell(int(row), col, "O")
    else:
        print("That cell is already taken")
        takeTurn(turn, currentBoard)
    


main()