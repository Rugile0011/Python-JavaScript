import re

patern1 = 'R|[A-Z]'
patern2 = '\d*([A-Z][A-Z]+)'
patern3 = '\d{3}[1,8,4,6,3]'
patern4 = '.\d{3}\s\d\s\d{3}\s\d{4}'
patern5 = '.\d\s\d.\s\d{3}\s\d{4}'
patern6 = '.\d\s\d.\s\d{3}\s\d{4}|.\d{3}\s\d\s\d{3}\s\d{4}'
patern7 = '\w{2}\d{2}\s\d{4}\s\d{4}\s\d{4}'
patern8 = '\w{2}\d{9}'
#patern9 = zodziai pries dvitaski
patern10 = '\w{4}.\w{8}.\w{2}'
patern11 = '[a-zA-Z-9._%-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}'


text = "Buveinės adresas: Konstitucijos pr. 20A, 03502 Vilnius" \
       "Telefonai:" \
       "1884 arba +370 5 268 4444 (Privatiems klientams) " \
       "1633 arba +370 5 268 4422 (Verslo klientams) " \
       "Faksas: (8 5) 258 2700" \
       "El. paštas: info@swedbank.lt" \
       "Įmonės kodas: 112029651" \
       "PVM mokėtojo kodas: LT120296515" \
       "Banko sąskaita: LT55 7300 0100 0000 0036" \
       "Banko kodas: 73000" \
       "SWIFT kodas: HABALT22"

print(re.findall(pattern=patern1, string=text))
print(re.findall(pattern=patern2, string=text))
print(re.findall(pattern=patern3, string=text))
print(re.findall(pattern=patern4, string=text))
print(re.findall(pattern=patern5, string=text))
print(re.findall(pattern=patern6, string=text))
print(re.findall(pattern=patern8, string=text))
#print(re.findall(pattern=patern9, string=text))
print(re.findall(pattern=patern10, string=text))
print(re.findall(pattern=patern11, string=text))
