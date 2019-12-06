from account import Account

account = Account('Rinald', 1234)  # balance = 0 by default
account.report()

print()
account.deposit(1000)  # balance = 1000
account.withdraw(700)  # balance = 1000-700 = 300
account.withdraw(1000)  # insuficient funds, balance = 300
print()

account.report()
