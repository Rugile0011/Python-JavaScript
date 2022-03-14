def fibonacci_sequence(range_):
    counter = 0
    fibonacci_number = [0, 1]

    while counter < range_:
        previous_number = fibonacci_number[-2]
        current_number = fibonacci_number[-1]
        print(fibonacci_number)

        if counter == 0:
            yield previous_number, current_number
        else:
            yield current_number

        amount = previous_number + current_number
        fibonacci_number.append(amount)
        counter += 1


counter = fibonacci_sequence(15)
for i in counter:
    print(i)
