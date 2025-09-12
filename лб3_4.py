class BankAccount:#создание класса BankAccount(банковский счет)
    def __init__(self):#конструктор класса-специальный метод который вызывается при созданий нового объекта 
        self._balance = 0 # инициализация защищенного атрибута для хранения баланса 
        self._transactions = []#инициализация списка для хранения истории транзакций 

    @property#декоратор свойства-превращает метод в свойство (можно обращаться как к свойству )
    def balance(self):# метод-геттер для получения баланса. Благодаря декоратору @propetory можно обращаться как acc balance 
        return self._balance# возвращает текущее значение защищенного атрибута 

    def deposit(self, amount):#метод для пополнения счета amount-сумма для пополнения 
        self._balance += amount#увеличивает баланс на указанную сумму 
        self._transactions.append(f"Deposit: +{amount}")# добовляет запись в историю транзакций 

    def withdraw(self, amount):# метод для снятия денег со счета 
        if amount > self._balance:# проверка достаточно ли денег на счете для снятия 
            self._transactions.append(f"Withdrawal failed: insufficient funds")# добовляет запись о неудачной попытке снятия 
            return False # операция не выполнена 
        self._balance -= amount # уменьшает баланс на сумму снятия 
        self._transactions.append(f"Withdrawal: -{amount}")# добовляет запись об успешном снятий 
        return True#операция выполнена 


# Пример использования
acc = BankAccount()
acc.deposit(1000)
acc.withdraw(500)

print(f"Balance: {acc.balance}")  # Balance: 500
