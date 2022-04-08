import os
from datetime import datetime

path = 'C:/Users/Rugilė/Desktop/Naujas Katalogas'

try:
    os.mkdir(path)
    print("Folder created!")
except FileExistsError:
    print("file already created.")

with open(r'C:\Users\Rugilė\Desktop\Naujas Katalogas\Tekstas5.txt', "w") as f:
    time_format = "%m/%d/%Y, %H:%M:%S"
    date_time = datetime.today().strftime(time_format)
    f.write(date_time)

created = os.stat(r'C:\Users\Rugilė\Desktop\Naujas Katalogas\Tekstas5.txt').st_ctime
print(datetime.fromtimestamp(created))
file_size = os.path.getsize(r'C:\Users\Rugilė\Desktop\Naujas Katalogas\Tekstas5.txt')
print("File Size is :", file_size, "bytes")
