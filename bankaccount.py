# Napisz klasę BankAccount, która implementuje podstawowe operacje na koncie
#  bankowym, takie jak wpłacanie, wypłacanie i sprawdzanie salda. Klasa powinna
#  wywoływać wyjątek przy próbie wpłaty lub wypłaty niepoprawnej kwoty. Następnie napisz
#  testy jednostkowe za pomocą PyTest, które sprawdzą poprawność działania metod oraz
#  obsługę błędów.

class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance = 0) -> None:
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount < 1:
            raise InvalidAmountError("You need to deposit at least $1.")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount < 1:
            raise InvalidAmountError("You can't withdraw 0 or negative amount of money.")
        
        if amount > self.balance:
            raise InsufficientFundsError("You don't have enough money.")
        
        self.balance -= amount;        
    
    def check_balance(self): 
        return self.balance
    