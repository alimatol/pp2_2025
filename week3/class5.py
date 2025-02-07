class BankAccount:
  
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
    else:
      pass

  def withdraw(self, amount):
    if self.balance > amount:
      self.balance -= amount
    else:
      pass


account = BankAccount("Bob", 4500)
account.deposit(400)
account.withdraw(100)

print(account.balance)
