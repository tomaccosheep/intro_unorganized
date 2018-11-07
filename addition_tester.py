#addition_tester.py
import random
num1 = random.randint(1, 5)
num2 = random.randint(1, 5)
user_answer = input(f"What is {num1} + {num2}? >")
user_answer = int(user_answer)
while True:
    if num1 + num2 == user_answer:
        print("Correct!")
        break
    elif user_answer > num1 + num2:
        print("Too much!")
    elif user_answer < num1 + num2:
        print("Too little!")
    user_answer = input(f"What is {num1} + {num2}? >")
    user_answer = int(user_answer)
