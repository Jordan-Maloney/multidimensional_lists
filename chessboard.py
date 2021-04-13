##
# chessboard.py
# Jordan Maloney
# 31/3/21

def chessboard():
    """
    Print a list of all chessboard values from A1 to H8
    """
    row = []
    MAX_SIZE = 8
    for i in range(MAX_SIZE):
        col = []
        row.append(col)
        for j in range(MAX_SIZE):
            row[i].append((i, j))
    return row

def display_board(board):
    ROW = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(ROW[j] + str(8-i), end = " ")
        print()

# Main routine
if __name__ == "__main__":
    board = chessboard()
    display_board(board)
