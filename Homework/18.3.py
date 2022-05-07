list = [2.5, 2, "Hello", True, 5, 7, 8, 2.8, "Evening"]

int_together = [x for x in list if type(x) == int]
print(sum(int_together))

str_together = " ".join([x for x in list if type(x) == str])
print(str_together)

B = sum(type(x) is bool for x in list)

print(B)
