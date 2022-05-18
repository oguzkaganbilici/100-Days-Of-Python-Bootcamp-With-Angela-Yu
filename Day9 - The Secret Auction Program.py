import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
                         
                          (bonggggg)
                         
                    BIDDING HAS STARTED
'''

medal = '''
 _______________
|@@@@|     |####|
|@@@@|     |####|
|@@@@|     |####|
\@@@@|     |####/
 \@@@|     |###/
  `@@|_____|##'
       (O)
    .-'"'"'-.
  .'  * * *  `.
 :  *       *  :
: ~    BIND   ~ :
: ~ A W A R D ~ :
 :  *       *  :
  `.  * * *  .'
    `-.....-'
'''
xx = {}
flag = True

while flag:
    print(logo)
    name = input("What is your name: ").capitalize()
    bid = int(input("What's your bid: $"))
    xx[name] = bid
    control = input("Are there any other bidders? Y/N: ").lower()
    if control == "y":
        os.system('clear')
    else:
        flag = False

def get_key(val):
    for key, value in xx.items():
        if value == val:
            return key
        
max_total = max(xx.values())
name = get_key(max_total)

os.system("clear")
print(medal)
print(f"The winner is {name} with a bid of ${max_total}")
  