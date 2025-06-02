
board = [" ", " ", " ", " "," ", " ", " ", " ", " "]

def print_dashboard():
    print("\n")
    print(f"  {board[0]}      {board[1]}      {board[2]} \n")
    print("---- | ----- | ---- \n")
    print(f"  {board[3]}      {board[4]}      {board[5]} \n")
    print("---- | ----- | ---- \n")
    print(f"  {board[6]}      {board[7]}      {board[8]} \n")
    print("---- | ----- | ---- \n")

def calcular_player_board():
    dashboard_player1 = []
    dashboard_player2 = []

    for i in range(len(board)):
        if board[i] == "X":
            dashboard_player1.append(i)
        elif board[i] == "O":
            dashboard_player2.append(i)
    return dashboard_player1,dashboard_player2

def calcular_win(list_player):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[6,4,2]]
    for list in wins:
        if set(list).issubset(list_player):
            return True
    return False


def play_game():
    game_is_over = False
    while not game_is_over:
        print_dashboard()
        player1_num = int(input("Choose your number between 0 - 8 "))
        board[player1_num] = "X"
        d1,d2 = calcular_player_board()
        print_dashboard()
        if calcular_win(d1):
            game_is_over = True
            print_dashboard()
            print("player 1 win")
            return

        player2_num = int(input("Choose your number between 0 - 8 "))
        board[player2_num] = "O"
        d1,d2 = calcular_player_board()
        if calcular_win(d2):
            game_is_over = True   
            print_dashboard()
            print("player 2 win")
            return
        print_dashboard()

        


    

while input("Do you want to play the game type: y or n ") == "y" :
    board = [" ", " ", " ", " "," ", " ", " ", " ", " "]
    play_game()