PIN = '0012'
def pin_code_generator(n):
    pin = 0
    for pin in range(n):
        str_pin = str(pin).zfill(4)
        yield str_pin

        if str_pin == PIN:
            print(f"PIN is {PIN}")
            break

        pin += 1


for pin in pin_code_generator(9999):
    print(pin)
