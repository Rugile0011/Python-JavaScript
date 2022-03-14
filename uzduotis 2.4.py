import random

dice1 = random.randrange(1, 6)
dice2 = random.randrange(1, 6)
dice3 = random.randrange(1, 6)

print("The value are:")
print("Dice 1 =", dice1, "Dice 2 =", dice2, "Dice 3 =", dice3)

while True:
    if dice1 or dice2 or dice3 == 5:
        print("Pralaimejai!")
        break
    else:
        print("Laimejai!")

# Klausimas: bet kuriuo atveju raso "Pralaimejai!"
