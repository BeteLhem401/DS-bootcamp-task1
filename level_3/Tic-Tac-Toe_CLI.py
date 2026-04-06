board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def show():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

player = "X"

for turn in range(9):
    show()
    pos = int(input("Choose position (1-9): ")) - 1

    if board[pos] == " ":
        board[pos] = player

        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("Taken")

show()
print("Game Over")
