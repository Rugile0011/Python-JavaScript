year = int(input("Enter the year you want to check: "))

if ((year%400 == 0)or ((year%4 == 0 ) and (year%100 != 0))):
    print("%d Leap year" %year)
else:
    print("%d Not leap year" %year)
