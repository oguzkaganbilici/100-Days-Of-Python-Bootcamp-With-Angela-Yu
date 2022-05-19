# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:24:33 2022

@author: 061885
"""

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random,os

def dealCards(player):
    card1,card2 = random.choices(cards, k = 2)
    player.append(card1)
    player.append(card2)
    
def newCard(player):
    newCard = random.choice(cards)
    player.append(newCard)
    
def total(player):
    if sum(player) == 21 and len(player) == 2:
        return 21
    if 11 in player and sum(player) > 21:
        player.remove(11)
        player.append(1)
    return sum(player)

def display(player, computer):
    total1 = total(player)
    total2 = total(computer)
    print(f" Your cards {player1}, current score: {total1}")
    print(f" Computer's cards: {computer}, computer score: {total2}")
    

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

player1 = []
computer = []
dealCards(player1)
dealCards(computer)

total1 = total(player1)
total2 = total(computer)
print(logo)

print(f" Your cards {player1}, current score: {total1}")
print(f" Computer's first card: {computer[0]}")

flag = True
while flag:
    total1 = total(player1)
    total2 = total(computer)
    if total == 21:
        print("Black Jack. You Won!")
        display(player1, computer)
        flag = False
    elif total2 == 21:
        os.system("clear")
        print(logo)
        print("Computer has made BlackJack. You Lost!")
        display(player1, computer)
        flag = False
    else:
        if input("Do you wanna take a card? (y): ") == "y":
            os.system("clear")
            print(logo)
            newCard(player1)
            newCard(computer)
            total1 = total(player1)
            total2 = total(computer)
            if total1 == 21:
                print("Black Jack. You Won!")
                display(player1, computer)
                flag = False
    
            elif total1 > 21:
                display(player1, computer)
                print("You lost!")
                flag = False
            
            elif total2 == 21:
                print("Computer has made BlackJack. You Lost!")
                display(player1, computer)
                flag = False
    
            elif total2 > 21:
                display(player1, computer)
                print("Computer lost!")
                flag = False
            else:
                print(f" Your cards {player1}, current score: {total1}")
                print(f" Computer's first card: {computer[0]}")
        else:
            os.system("clear")
            print(logo)
            player_last = 21 - total1
            comp_last = 21 - total2
            if player_last < comp_last:
                display(player1, computer)
                print("You Won")
                flag = False
            elif player_last == comp_last:
                display(player1, computer)
                print("Draw")
                flag = False
            else:
                display(player1, computer)
                print("You Lost")
                flag = False
             