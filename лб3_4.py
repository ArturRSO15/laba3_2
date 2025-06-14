class BankAccount:
    def __init__(self):
        self._balance = 0
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if amount > self._balance:
            self._transactions.append(f"Withdrawal failed: insufficient funds")
            return False
        self._balance -= amount
        self._transactions.append(f"Withdrawal: -{amount}")
        return True


# Пример использования
acc = BankAccount()
acc.deposit(1000)
acc.withdraw(500)
print(f"Balance: {acc.balance}")  # Balance: 500