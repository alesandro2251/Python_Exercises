import unittest

class Account:
    def __init__(self, _id, name, balance=0):
        self.id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += int(amount)

        return self.balance

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount

            return self.balance
        else:
            return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


# Unit Test for Account class
class TestAccount(unittest.TestCase):

    def setUp(self):
        # This method will run before every test
        self.account = Account(1, 'John Doe', 100)

    def test_credit(self):
        self.account.credit(50)
        self.assertEqual(self.account.balance, 150)  # Initial 100 + 50

    def test_debit_success(self):
        self.account.debit(50)
        self.assertEqual(self.account.balance, 50)  # Initial 100 - 50

    def test_debit_failure(self):
        result = self.account.debit(150)
        self.assertEqual(result, "Amount exceeded balance")
        self.assertEqual(self.account.balance, 100)  # Balance should remain unchanged

    def test_info(self):
        self.assertEqual(self.account.info(), "User John Doe with account 1 has 100 balance")

# Run the unit tests
if __name__ == "__main__":
    unittest.main()
