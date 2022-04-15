username = input('what is your username?')
password = input('what is your password?')
password_lenght = len(password)
hidden_password = '*' * password_lenght


print(f'{username}, your password: {hidden_password}.  Is {password_lenght} letters long')
