class BankAccount():
    """Class definition of a bank account"""

    def __init__(self, name="", balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdrawal(self, withdrawal):
        self.balance -= withdrawal

    def display_infos(self):
        print(f'The bank account of {self.name} has a balance of {self.balance}')


mike_account = BankAccount('Mike', 1000)
mike_account.deposit(2500)
mike_account.display_infos()

susan_account = BankAccount('Susan')
susan_account.withdrawal(600)
susan_account.display_infos()