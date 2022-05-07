word = []
for i in range(5):
    z = input("Input word: \n")
    zodis.append(z)
print(word)


lenght_sentence0 = len(word[0])
print("First word lenght:", lenght_sentence0)
lenght_sentence1 = len(word[1])
print("Second word lenght:", lenght_sentence1)
lenght_sentence2 = len(word[2])
print("Third word lenght:", lenght_sentence2)
lenght_sentence3 = len(word[3])
print("Fourth word lenght:", lenght_sentence3)
lenght_sentence4 = len(word[4])
print("Fifth word lenght:", lenght_sentence4)

n = 1
for item in word:
    print(n, item)
    n += 1
