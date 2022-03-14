import smtplib
from email.message import EmailMessage
import mimetypes
from string import Template


def creat_email(from_, to_, subject):
    email_message = EmailMessage()
    email_message["from"] = from_
    email_message["to"] = to_
    email_message["subject"] = subject
    return email_message


def attach_file(email_message, files):
    for file in files:
        mimetype = mimetypes.guess_type(file)[0]
        subtype = mimetype.split("/")[1]
        with open(file, "rb") as img:
            content = img.read()
            email_message.add_attachment(
                content,
                maintype=mimetype,
                subtype=subtype,
                filename=file)


def sending_email(email_message, email_address, password, smtp, smtp_port):
    with smtplib.SMTP(host=smtp, port=smtp_port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email_address, password)
        smtp.send_message(email_message)


def main(email_address,
         password,
         smtp,
         smtp_port,
         from_,
         to_,
         subject,
         content=None,
         html=None,
         substitute=None,
         files=None):
    email_message = creat_email(from_, to_, subject)

    if content:
        email_message.set_content(content)
    elif html and substitute:
        template = Template(html)
        email_message.set_content(template.substitute({"vardas": substitute}), "html")
    else:
        raise ValueError("Provide content or html and substitute")

    if files:
        attach_file(email_message, files)
    else:
        pass

    sending_email(email_message, email_address, password, smtp, smtp_port)
