import numpy as np

array = np.arange(1, 101)


def prime_or_not(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True


new_function = np.vectorize(array)
print(prime_or_not(3))

# print(prime_or_not(new_function))
