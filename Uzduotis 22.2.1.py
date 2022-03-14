import datetime

datetime_object = datetime.datetime.strptime('2019.04.15', '%Y.%m.%d')
datetime_output = datetime_object.strftime('%Y %m %d')

print(datetime_output)