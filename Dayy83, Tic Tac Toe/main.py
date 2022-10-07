import os

coordinates = {"a": "a", "b": "b", "c": "c",
               "d": "d", "e": "e", "f": "f",
               "g": "g", "h": "h", "i": "i",
                }


def show_board():
    board = f""" 
                ░▀█▀░▀█▀░█▀▀░░░▀█▀░█▀█░█▀▀░░░▀█▀░█▀█░█▀▀
                ░░█░░░█░░█░░░░░░█░░█▀█░█░░░░░░█░░█░█░█▀▀
                ░░▀░░▀▀▀░▀▀▀░░░░▀░░▀░▀░▀▀▀░░░░▀░░▀▀▀░▀▀▀

                {coordinates["a"]} | {coordinates["b"]} | {coordinates["c"]}
                ___________
                {coordinates["d"]} | {coordinates["e"]} | {coordinates["f"]}
                ------------
                {coordinates["g"]} | {coordinates["h"]} | {coordinates["i"]}
                """
    return board


def check_win():
    if (coordinates["a"] == coordinates["b"] == coordinates["c"]) or\
       (coordinates["d"] == coordinates["e"] == coordinates["f"]) or\
       (coordinates["g"] == coordinates["h"] == coordinates["i"]):
        return False
    elif (coordinates["a"] == coordinates["d"] == coordinates["g"]) or\
         (coordinates["b"] == coordinates["e"] == coordinates["h"]) or\
         (coordinates["c"] == coordinates["f"] == coordinates["i"]):
        return False
    elif (coordinates["a"] == coordinates["e"] == coordinates["i"]) or\
         (coordinates["c"] == coordinates["e"] == coordinates["g"]):
        return False
    else:
        return True


def check_availability(x):
    if coordinates[x] == "X":
        return False
    elif coordinates[x] == "O":
        return False
    else:
        return True


flag = True
while flag:
    for i in range(len(coordinates)):
        os.system("cls")
        print(show_board())
        player1 = input("Player1: ")
        flag_player1 = check_availability(player1)
        while not flag_player1:
            os.system("cls")
            print("You can not pick that! Try again!")
            print(show_board())
            player1 = input("Player1: ")
            flag_player1 = check_availability(player1)
        coordinates[player1] = "X"
        flag = check_win()
        if not flag:
            os.system("cls")
            print(show_board())
            print("Player1 WON!")
            break
        os.system("cls")
        print(show_board())
        player2 = input("Player2: ")
        flag_player2 = check_availability(player2)
        while not flag_player2:
            os.system("cls")
            print("You can not pick that! Try again!")
            print(show_board())
            player2 = input("Player2: ")
            flag_player2 = check_availability(player2)
        coordinates[player2] = "O"
        flag = check_win()
        if not flag:
            print(show_board())
            print("Player2 WON!")
            break
