
def sum(a, b, c):
    return a + b + c

def printboard(xstate, zstate):
    zero = 'X' if xstate[0] else ('O' if zstate[0] else ' ')
    one = 'X' if xstate[1] else ('O' if zstate[1] else ' ')
    two = 'X' if xstate[2] else ('O' if zstate[2] else ' ')
    three = 'X' if xstate[3] else ('O' if zstate[3] else ' ')
    four = 'X' if xstate[4] else ('O' if zstate[4] else ' ')
    five = 'X' if xstate[5] else ('O' if zstate[5] else ' ')
    six = 'X' if xstate[6] else ('O' if zstate[6] else ' ')
    seven = 'X' if xstate[7] else ('O' if zstate[7] else ' ')
    eight = 'X' if xstate[8] else ('O' if zstate[8] else ' ')
    
    print(f"{zero} | {one} | {two}")
    print("--|---|--")
    print(f"{three} | {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eight}")

def checkwin(xstate, zstate):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            print("X won the match")
            return 1
        if sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3:
            print("O won the match")
            return 0
    return -1

def reset_board():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0]

if __name__ == "__main__":
    play_again = True
    print("Welcome to Tic Tac Toe")
    while play_again:
        xstate = reset_board()
        zstate = reset_board()
        turn = 1  # 1 for X and 0 for O
       

        while True:
            printboard(xstate, zstate)
            
            if turn == 1:
                print("X's chance")
            else:
                print("O's chance")

            value = int(input("Please enter value: "))
            
            if xstate[value] == 0 and zstate[value] == 0:
                if turn == 1:
                    xstate[value] = 1
                else:
                    zstate[value] = 1
            else:
                print("Invalid move. Try again.")
                continue

            cwin = checkwin(xstate, zstate)
            if cwin != -1:
                printboard(xstate, zstate)
                print("Match over")
                break

            turn = 1 - turn

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'
