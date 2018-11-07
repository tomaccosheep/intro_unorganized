#catch_not_cat.py
while True:
    var1 = input("Please type cat >")
    if var1 == 'cat':
        break

var2 = 5
while var2 != 'dog': #If the answer isn't correct, repeat with "True"
    var2 = input("Please type dog >")
