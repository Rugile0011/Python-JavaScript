my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in my_list:
    counter = counter + item
print(counter)


def highest_even(list):
    evens = []
    for item in list:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 1, 2, 3, 4, 8, 11]))
