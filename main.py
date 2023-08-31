print("Let's play Heads or Tails...\n")
import random
random_side = random.randint(0,1)
input('Write "T" to Throw the coin.\n').upper()
if "T":
  if random_side == 0:
    print("\n" + "Heads" + "\n")
  elif random_side == 1:
    print("\n" + "Tails" + "\n")
print("\nPress Run to play again")