#A simple non-GUI sudoku solver that employs the backtracking algorithm.
# A 2D array was used to create the board.Empty cells are represented with "0".
sudoku_board = [
              [7,6,0,0,0,9,3,0,0],
              [3,1,0,0,0,0,5,0,0],
              [0,0,4,0,7,0,0,6,0],
              [4,3,0,1,0,6,0,0,8],
              [8,7,0,0,4,0,0,3,1],
              [6,0,0,8,0,7,0,5,9],
              [0,5,0,0,9,0,1,0,0],
              [0,0,7,0,0,0,0,2,3],
              [0,0,6,2,0,0,0,4,5],
]

#A function to solve the given board
def solver(board):
    find = find_empty_cell(board)
    #if we do not find an empty cell
    if not find:
        return True
    else:
      #locating current empty cell to work with.
        row,col = find
    #trying out all numbers between 1 and 9
    for i in range(1,10):
        if is_valid(board,i,(row,col)):
            board[row][col]=i
#applying recursion to solve the board
            if solver(board):
                return True

            board[row][col] = 0
    return False                    

#Function to make sure the guess at each instance is actually valid
def is_valid(board,num,pos):
    #checking the rows
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #checking columns
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #checking each cell
    cell_x = pos[1] // 3
    cell_y = pos[0] // 3

    for i in range(cell_y *3, cell_x*3 + 3):
        for j in range(cell_x *3, cell_y*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True            

              
#prints the board with "*" separating every 3 rows and "|" separating every 3 values in a row.
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("************************")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0: 
                print(" | ", end="")

            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ",end= "")    
                 
#Function to find empty cells
def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
            # returns the value of the row and column of the empty cell
                return(i,j)
    return None


if __name__ == "__main__":
    print("sudoku puzzle given")
    #unsolved sudoku puzzle
    print_board(sudoku_board)

#calling the sudoku solver
    solver(sudoku_board)

    print("sudoku puzzle solved "
          ""
          ""
          "\n")
    #showing the solved sudoku puzzle
    print_board(sudoku_board)
