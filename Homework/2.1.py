#sukurti zodyna ir sarasa
d = {
    "brand": "iphone",
    "model": "X",
    "year": 2017}

s = [1, 2, 3, 4, 5]

#atspausdinti reiksme
print(s[0])
print(d["brand"])

#pridesti reiksme
d["color"] = "black"
print(d)

s.append(6)
print(s)

#istrinti reiksme
del d["brand"]
print(d)

del s[2]
print(s)

#pakeisti irasa

s[0] = 0
print(s)

d["year"] = 2020
print(d)


