enterfile = input("Enter the input file name: ") + ".txt"
file = open(enterfile, "a+")

while True:
    num = int(input("Enter a line number [0 to quit]: "))
    if num >= 1:
        for i in range(num):
            z = input("Iveskite zodi: \n")
            file.write(z)
    elif num == 0:
        break

#nesigavo atspausdinti txt faile zodziu atskirose eilutese
