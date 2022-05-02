import datetime
import pandas as pd
import smtplib
import ssl
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM


def email_func(subject, birthday_receiver, name):
    receiver = birthday_receiver
    sender = 'rugileudemy@gmail.com'
    sender_password = 'UdemyRugileUdemy01'

    msg = MM()
    msg['Subject'] = 'Birthday remainder: ' + name + ' ' + subject + ' ' + upcoming_birthday.strftime('%B %d') + '!'

    HTML = f"""
  <html>
    <body>
      <h1>Hi,
        This is a reminder that {name} will be celebrating birthday soon!
        There are {days_left} days left to get a present!</h1>
      <img src="https://th.bing.com/th/id/R.378dd037b2ad5e3f47feae2a52b0399f?rik=k%2bsMti7viEfmGA&riu=http%3a%2f%2fcdn.wallpapersafari.com%2f74%2f60%2fQ75pNS.jpg&ehk=0PRCXnm9iBuaM62boTRFIrGn3KdHem7trJVwO%2fPi1eI%3d&risl=&pid=ImgRaw&r=0" alt ="Image" width="600" height="300"></img>
    </body>
  </html>
"""

    MTObj = MT(HTML, "html")
    msg.attach(MTObj)
    SSL_context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=SSL_context)
    server.login(sender, sender_password)
    server.sendmail(sender, receiver, msg.as_string())


def birthday_checker(df):
    year = today.year
    for i in range(0, len(df)):
        month = df['Birth_Month'][i]
        day = df['Birth_Day'][i]
        birthday = datetime.date(year, month, day)
        print(f"remainder time: {upcoming_birthday} birthday: {birthday}")
        if upcoming_birthday == birthday:
            return df.iloc[i]
    print("Birthday after 7 days is not found")


def send_birthday_notification(df):
    birthday_person = birthday_checker(df)
    if birthday_person is None:
        return None
    birthday_person_name = birthday_person['Name']
    birthday_person_email = birthday_person['Email']
    for i in range(0, len(df)):
        email = df['Email'][i]
        if email is not birthday_person_email:
            email_func('birthday is coming soon on', email, birthday_person_name)


data = pd.read_excel('info3.xlsx')
today = datetime.date.today()
upcoming_birthday = today + datetime.timedelta(days=7)
days_left = (upcoming_birthday - today).days
send_birthday_notification(data)
