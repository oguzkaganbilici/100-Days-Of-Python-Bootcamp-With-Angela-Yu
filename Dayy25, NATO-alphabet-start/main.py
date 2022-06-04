import pandas as pd

dt = pd.read_csv("nato_phonetic_alphabet.csv")

nato = {rows.letter:rows.code for index,rows in dt.iterrows()} 
#index and rows in for is not important. you can change it with outside for loop
#like: {row.letter:row.code for sdfafdasd,row in dt.iterrows}

user_input = input("Type a word:")
word = [i for i in user_input]

letters = [nato[letter.upper()] for letter in word]
print(letters)


