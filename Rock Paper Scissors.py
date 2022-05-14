import random



rock = '''
        ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
        PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
        SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
score_player = 0
score_computer = 0

while 1:
    a = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS:\n"))
    b = random.randint(0, 2)
    
    if a == 0:
        if b == 0:
            print("You Choose: ", rock)
            print("Computer Choose: ", rock)
            print("Draw, try again!")

        
        elif b == 1:
            print("You Choose: ", rock)
            print("Computer Choose: ", paper)
            print("You Lost, loser!")
            score_computer += 1
        elif b == 2:
            print("You Choose: ", rock)
            print("Computer Choose: ", scissors)
            print("You Won!")
            score_player += 1
    
    elif a == 1:
        if b == 0:
            print("You Choose: ", paper)
            print("Computer Choose: ", rock)
            print("You Won!")
            score_player += 1
    
        elif b == 1:
            print("You Choose: ", paper)
            print("Computer Choose: ", paper)
            print("Draw, try again!")
        elif b == 2:
            print("You Choose: ", paper)
            print("Computer Choose: ", scissors)
            print("You Lost, loser")
            score_computer += 1
            
    elif a == 2:
        if b == 0:
            print("You Choose: ", scissors)
            print("Computer Choose: ", rock)
            print("You Lost, loser")
            score_computer += 1
    
        
        elif b == 1:
            print("You Choose: ", scissors)
            print("Computer Choose: ", paper)
            print("You Won!")
            score_player += 1
    
        elif b == 2:
            print("You Choose: ", scissors)
            print("Computer Choose: ", scissors)
            print("Draw, try again!")
        
    print(f"You: {score_player}")
    print(f"Computer: {score_computer}")
    
    if score_player == 5 or score_computer == 5:
        break
    
if score_computer > score_player:
    print("You lost the game, big loser\n")
else:
    print("Congrats winner!\n")





















