from datetime import datetime, timedelta

date_5 = datetime.now() - timedelta(5)
date_8 = datetime.now() + timedelta(8)

print('Current Date :',datetime.now())
print('5 days before Current Date :', date_5)
print('plus 8 days to Current Date :', date_8)

now = datetime. now()
time_format = now.strftime("%Y %m %d, %H:%M:%S")
print(time_format)