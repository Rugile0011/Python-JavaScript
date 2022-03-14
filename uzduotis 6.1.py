class Sakinys:
    def __init__(self, text):
        self.text = text

    def backwards(self):
        result = self.text[::-1]
        return result

    def lower_text(self):
        result = self.text.lower()
        return result

    def upper_text(self):
        result = self.text.upper()
        return result

    def text_count(self):
        result1 = self.text.split()
        result2 = len(result1)
        return result2

    def line(self, kint):
        result = self.text.split()[kint]
        return result

    def replace(self, replace_1, replace_2):
        result = self.text.replace(replace_1, replace_2)
        return result

    def analysis(self):
        abc_split = self.text.split()
        number = 0
        upper = 0
        lower = 0
        for i in self.text:
            if i.islower():
                lower += 1
            if i.isupper():
                upper += 1
            if i.isdigit():
                number += 1

        print(
            f"words == {len(abc_split)} upper= {upper}, lower = {lower}, number == {number}")


text1 = Sakinys('Didelis KamuolyS')
backwards1 = text1.backwards()
lower_text1 = text1.lower_text()
upper_text1 = text1.upper_text()
words1 = text1.text_count()
line1 = text1.line(1)
replace1 = text1.replace('i', 'e')

print(backwards1)
print(lower_text1)
print(upper_text1)
print(words1)
print(line1)
print(replace1)
