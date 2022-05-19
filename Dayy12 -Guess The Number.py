# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:26:37 2022

@author: 061885
"""
import random,os
logo = """
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
  """                           
print(logo)                                                             
print("I guessed the number between 0 and 100.")
number = random.randint(0, 100)
choice = input("Choose a diffuculty. Type 'e' for easy, type 'h' for hard: ")
if choice == "e":
    life = 10
elif choice == "h":
    life = 5

flag = True
while flag:
    os.system("clear")
    print(logo)
    guess = int(input("Make a guess: "))
    life = life -1
    if guess == number:
        print("Congratz. You found it.")
        flag = False
    elif guess > number:
        print("Too High")
        print(f"You have {life} remaning to guess the number.")
    else:
        print("Too Low")
        print(f"You have {life} remaning to guess the number.")
    input("press enter")