from bankaccount import *
import pytest

def test_initial_balance():
    account = BankAccount(100)
    assert account.check_balance() == 100

def test_default_initial_balance():
    account = BankAccount()
    assert account.check_balance() == 0

def test_initial_negative_balance():
    with pytest.raises(InvalidAmountError):
        BankAccount(-100)

def test_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.check_balance() == 150

def test_deposit_negative_amount():
    account = BankAccount(100)
    with pytest.raises(InvalidAmountError):
        account.deposit(-50)
        
def test_deposit_zero_amount():
    account = BankAccount(100)
    with pytest.raises(InvalidAmountError):
        account.deposit(0)

def test_withdraw():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.check_balance() == 50

def test_withdraw_negative_amount():
    account = BankAccount(100)
    with pytest.raises(InvalidAmountError):
        account.withdraw(-50)
        
def test_withdraw_zero_amount():
    account = BankAccount(100)
    with pytest.raises(InvalidAmountError):
        account.withdraw(0)

def test_withdraw_insufficient_funds():
    account = BankAccount(100)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(150)

def test_get_balance():
    account = BankAccount(100)
    assert account.check_balance() == 100


if __name__ == "__main__":
    pytest.main()

