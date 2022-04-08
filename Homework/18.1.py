s = "The Zen of Python"

def add_exclamation_mark(s):
    return f"{s} ! "

print("".join(map(add_exclamation_mark, s.split())))
