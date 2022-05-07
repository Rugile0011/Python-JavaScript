theSum = 0

while True:
    number = int(input("Input number:"))
    if number < 0:
        break
    theSum += number

print("Sum of input:", theSum)
