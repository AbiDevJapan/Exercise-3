# Add the following code to the master branch: if heads win, the program prints the message You won, otherwise it prints the message You lost. Commit this revision with the message “Victory message added”.

import random

print("Tossing a coin...")
heads = 0
tails = 0

for i in range(1, 4):
    if random.randint(0, 1) == 0:
        print(f"Round {i}: Heads")
        heads += 1
    else:
        print(f"Round {i}: Tails")
        tails += 1
        
print(f"Heads: {heads}, Tails: {tails}")

if heads > tails:
    print("You won")
else:
    print("You lost")
    