def getnums(s, e):
    return list(range(s, e))

start, end = 0, 50
numlist = (getnums(start, end))
print(numlist)

newlist = map(lambda x: x * 10, numlist)
print(newlist)
print(list(newlist))


def seven(numlist):
    newlist_2 = []
    for skaicius in numlist:
        if skaicius % 7 == 0:
            newlist_2.append(skaicius)
    return newlist_2

print(seven(numlist))


newlist_3 = map(lambda x: x**2, numlist)
print(list(newlist_3))


Sum = sum(map(lambda x: x**2, numlist))
print(Sum)
print(min(map(lambda x: x**2, numlist)))
print(max(map(lambda x: x**2, numlist)))

from statistics import mean

avg = mean((map(lambda x: x**2, numlist)))
print("The average is ", round(avg, 2))

import statistics

print("Median of data-set is : % s "
        % (statistics.median(map(lambda x: x**2, numlist))))

newlist_4 = list(map(lambda x: x**2, numlist))
newlist_4.reverse()
print('Updated List:', newlist_4)