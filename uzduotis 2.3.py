zodis = []
for i in range(5):
    z = input("Iveskite zodi: \n")
    zodis.append(z)
print(zodis)


lenght_sentence0 = len(zodis[0])
print("Pirmo zodzio ilgis:", lenght_sentence0)
lenght_sentence1 = len(zodis[1])
print("Antro zodzio ilgis:", lenght_sentence1)
lenght_sentence2 = len(zodis[2])
print("Trecio zodzio ilgis:", lenght_sentence2)
lenght_sentence3 = len(zodis[3])
print("Ketvirto zodzio ilgis:", lenght_sentence3)
lenght_sentence4 = len(zodis[4])
print("Penkto zodzio ilgis:", lenght_sentence4)

n = 1
for irasas in zodis:
    print(n, irasas)
    n += 1