banking_account = []
balance = []
name_account = "quit"

while name_account == "quit":
    new_account = input("What is the name of this account? ")
    banking_account.append(new_account)
    
    if new_account.lower == "quit":
        banking_account.remove(new_account)
        break
    else:
        new_balance = float(input("What is the balance? "))
        balance.append(new_balance)

total = 0

for accounts in banking_account:
    print(accounts)


