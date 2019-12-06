class Account:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def get_name(self):
        return self.name

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance

    def deposit(self, ammount):
        self.balance += ammount

    def withdraw(self, ammount):
        if self.balance < ammount:
            print('Insuficient funds')
        else:
            self.balance -= ammount

    def report(self):
        print('Name:', self.name)
        print('PIN:', self.pin)
        print('Balance:', self.balance)
