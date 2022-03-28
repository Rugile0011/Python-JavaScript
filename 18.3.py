sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

int_together = [x for x in sarasas if type(x) == int]
print(sum(int_together))

str_together = " ".join([x for x in sarasas if type(x) == str])
print(str_together)

B = sum(type(x) is bool for x in sarasas)

print(B)
