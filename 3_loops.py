#3_loops.py

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for cat in range(0, 5, 2):
for cat in range(0, 5):
    print(cat)

# for dog in num_list[0:5:2]:
for dog in num_list[0:5]:
    print(dog)

rat = 0
while rat < 5:
    # one million lines of code
    user_in = input("What's the best movie? >")
    if user_in == "Whitecastle":
        break
    # rat = rat + 2
    rat = rat + 1
