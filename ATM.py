class Account:
  def __init__(self, owner, balance=0):
      self.owner = owner
      self.balance = balance
      
  def __str__(self):
      return (f'Account Owner: {self.owner} \nAccount Balance: {self.balance}')
      
  def deposit(self, dep_amt):
      self,balance += dep_amt
      print('Deposit Accepted')
      
  def withdraw(self, wd_amt):
      if self.balance >= wd_amt:
          self.balance -= wd_amt
          print ('Withdrawal Accepted')
      else:
          print ('Account not enough fund.')
