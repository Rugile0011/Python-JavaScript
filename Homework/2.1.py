
d = {
    "brand": "iphone",
    "model": "X",
    "year": 2017}

s = [1, 2, 3, 4, 5]

print(s[0])
print(d["brand"])


d["color"] = "black"
print(d)

s.append(6)
print(s)


del d["brand"]
print(d)

del s[2]
print(s)



s[0] = 0
print(s)

d["year"] = 2020
print(d)


