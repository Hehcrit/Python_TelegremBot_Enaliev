# Задаем значения для 2 игроков
player1 = "X"
player2 = "0"


# 3 х 3 игровое поле
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def draw_board(board):          # рисует простенькую доску(нужна доработка)
    print("---------")
    for i in range(3):
        print(" | ".join(board[i]))
        print("---------")


def ask_move(player, board):
    x, y = input(f"{player}, enter x and y coordinates (e.g. 0 0): ").strip().split()         # игрок вводит свой ход
    x, y = int(x), int(y)           # преобразование кода
    if (0 <= x <= 2) and (0 <= y <= 2):         # проверка границ игрового поля
        return (x, y)
    else:
        print("Клетка занята. Введите координаты еще раз.")
    return ask_move(player, board)


def make_move(player, board, x, y):         # проверяет свободна ли клетка и делает ход
    if board[x][y] != " ":
        print("Клетка занята!")
        return False
    board[x][y] = player
    return True


def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    make_move(player, board, x, y)


def check_win(player, board):       #ПРОВЕРКА ПОБЕДУКТЕЛЯ
    for i in range(3):
        if board[i] == [player, player, player]:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif  board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False


def tie_game():             #Условия ничьи
    for row in board:
        for cell in row:
            if cell == " ":
                return True
    return False


def tic_tac_toe():          #Игровой дирижер
    while True:
        player = player1
        while True:
            draw_board(board)
            ask_and_make_move(player, board)
            if check_win(player, board):
                print(f"{player} Выгрунтиватель!")
                break
            tie_game()          # Проверка на ничью
            if not tie_game:
                break
            player = player2 if player == player1 else player1
        restart = input("Хотите сыграть еще раз? (y/n) ")
        if restart.lower() != "y":
            break


tic_tac_toe()
# Нужнен дебаггинг кода