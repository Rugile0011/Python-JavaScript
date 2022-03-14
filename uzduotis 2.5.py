metai = int(input("Iveskite metus, kuriuos norite patikrinti: "))

if ((metai%400 == 0)or ((metai%4 == 0 ) and (metai%100 != 0))):
    print("%d Keliamieji" %metai)
else:
    print("%d Nekeliamieji" %metai)
