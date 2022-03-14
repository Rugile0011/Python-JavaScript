import os
from datetime import datetime
import json

text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

with open("Tekstas.txt", "w") as f:
    f.write(text)

with open("Tekstas.txt", "r") as f:
    data = f.read()
    print(data)

with open("Tekstas.txt", "a") as f:
    time_format = "\n%m/%d/%Y, %H:%M:%S"
    date_time = datetime.today().strftime(time_format)
    f.write(date_time)

with open("Tekstas.txt", "r") as f:
    eilutes = f.readlines()
    for i, eilute in enumerate(eilutes, start=1):
        print(i, eilute)

with open("Tekstas.txt", "r") as f:
    text = f.read()
    changed_text = text.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")
    print(changed_text)

with open("Tekstas.txt", "r") as f:
   text = f.read()
   backwards = text[::-1]
   print(backwards)

with open("Tekstas.txt", "r") as f:
   text = f.read()

   def analysis(txt):
       word_count = len(txt.split(" "))
       upper_letter_count= sum(1 for raide in txt if raide.isupper())
       lower_letter_count = sum(1 for raide in txt if raide.lower())
       print(f"""{word_count} {upper_letter_count} {lower_letter_count}""")

analysis(text)

with open("Tekstas.txt", "r") as f:
   text = f.read()
   text_upper = text.upper()

with open("Tekstas2.txt", "w") as f:
   f.write(text_upper)

with open("Tekstas2.txt", "r") as f:
   text = f.read()
   print(text)
