def number_generator():
    index = 2
    while True:
        yield index
        index += 2


gen = number_generator()
print(next(gen))
print(next(gen))
