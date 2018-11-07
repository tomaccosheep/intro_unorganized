#description_game.py
import os
noun = input("First type a word that both players agree on >")
max_len = input("Now think of how many descriptors you will both say >")
max_len = int(max_len)
player1_words = []
player2_words = []
for player in [player1_words, player2_words]:
    while len(player) < max_len:
        player.append(input(f"What word would you use to describe the word {noun}?"))
    os.system('clear')
player1_words.sort()
player2_words.sort()
print(player1_words)
print(player2_words)
if player1_words == player2_words:
    print("You win!")
else:
    print("You lose.")
