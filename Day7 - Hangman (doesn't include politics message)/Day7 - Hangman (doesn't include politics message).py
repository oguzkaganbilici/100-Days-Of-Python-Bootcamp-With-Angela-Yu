# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:19:15 2022

@author: 061885
"""
import random
from word_list import wordlist
from stage import stages

total_live = 6
false_inputs = []
word = wordlist[random.randint(0, len(wordlist)-1)]
word2 = []

for i in range(len(word)):
    word2.append("_")
print(word2)

while 1:
    print(stages[total_live])    
    user = input("\nGuess a letter: ")
    print(f"You guessed {user}")
    
    
    for i in range(len(word2)):
        letter = word[i]
        if letter == user:
            word2[i] = user

    if user not in word:
        false_inputs.append(user)
        total_live -= 1
        print(f"You spent lifes with {false_inputs}")
        
    print(word2)
    
    if total_live == 0:
        print("You lost!")
        print(f"Word is {word}")
        break
    
    elif "_" not in word2:
        print("you win")
        break