#candy_betting.py
import random
user_pennies = random.randint(200, 300)
user_candy = 0
while True:
    print(f"You have {user_pennies} pennies and {user_candy} pieces of candy.")
    user_choice = input("Would you like to make a (bet) with the store or (cash out)? >")
    while user_choice.lower() not in ['bet', 'cash out']:
        user_choice = input("Would you like to make a (bet) with the store or (cash out)? >")
    if user_choice.lower() == 'cash out':
        break
    else:
        bet_amount = int(input("How many $.25 pieces of candy are you betting? >"))
        if bet_amount * 25 > user_pennies:
            input("Too much!")
            continue
        if random.randint(0,1) == 0:
            print("You won!")
            user_candy = user_candy + bet_amount
        else:
            print("You lost!")
            user_pennies = user_pennies - (bet_amount * 25)
print("Cashing out")
user_candy = user_candy + (user_pennies // 25)
user_pennies = user_pennies % 25
print(f"You have {user_candy} pieces of candy and {user_pennies} pennies left over.")
