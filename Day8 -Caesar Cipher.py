alphabet = ['a', 'b', 'c', 'd', 'e', 
            'f', 'g','ğ','h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v','w', 'x', 'y', 'z']

art = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
import os

def Caesar(text_f, shift_f,direction):
    word = ""
    if direction == "e":
        for i in text_f:
            if i in alphabet:
                x  = alphabet.index(i)
                new_x = x + shift
                if new_x >= len(alphabet):
                    new_x = new_x % len(alphabet)
        
                word += alphabet[new_x]
            else:
                word += i
        return word
    elif direction == "d":
        for i in text_f:
            if i in alphabet:
                x = alphabet.index(i)
                new_pos = x - shift_f
                word += alphabet[new_pos]
            else:
                word += i
        return word


flag = True
while(flag == True):
    print(art)
    
    direction = input("Type e to encrypt, type d to decrypt: ")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    print(Caesar(text,shift,direction))
    control = input("\nDo you wanna continue to translate ?: ")
    if control == "n":
        print("Goodbye Soldier")
        flag = False
    else:
        os.system("clc")
    
    
