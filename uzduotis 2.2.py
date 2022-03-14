theSum = 0

while True:
    number = int(input("Iveskite skaiciu:"))
    if number < 0:
        break
    theSum += number

print("Ivestu skaiciu suma:", theSum)
