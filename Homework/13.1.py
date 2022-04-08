balance = 600

def withdraw():
    counter = 0
    while counter <= 2:
        while counter == 0:
            withdraw = int(input("Enter the amount you want to withdraw: "))
            counter = counter + 1
            withdraw2 = int(input("Enter the amount you want to deposit: "))
            counter = balance + counter
        while ((int(balance) - int(withdraw)) < 0):
            print("Error Amount not available in card.")
            withdraw = int(input("Please enter the amount you want to withdraw again: "))
            continue
        while ((float(balance) - float(withdraw)) >= 0):
            print("Amount left in your account: " + str(balance - withdraw + withdraw2))
            return (balance - withdraw)
        counter = counter + 1



list = [balance, withdraw()]
print(list)

#filename = "money.pkl"
#file = open(filename, 'wb')
#pickle.dump(list, file)
#file.close()

#file = open(filename, 'rb')
#new_list = pickle.load(file)
#file.close()

#print(new_list)
