from datetime import datetime

input_date = str(input('Enter date(yyyy-mm-dd hh:mm): '))
date = datetime.strptime(input_date, "%Y-%m-%d %H:%M")

print(date)

now = datetime.now()
print(now)
delta = now - date

print(float((now-date).days)/365)
print((now.year - date.year) * 12 + (now.month - date.month))
print(delta.days)
#praleidau valandas
print(delta.total_seconds()/60)
print(delta.total_seconds())
