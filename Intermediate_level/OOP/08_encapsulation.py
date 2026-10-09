# OOP encapsulation

# a program to keep the account balance inside the class and update it through a method.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    #kept the balance as a private attribute

    def deposit(self, amount):
        self.__balance += amount     #added the deposit to the current balance

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(1000)       #created an account with an initial balance

account.deposit(500)          #deposited 500 into the account
account.show_balance()           #displayed the updated balance