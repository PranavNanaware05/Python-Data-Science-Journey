class account:
    def __init__(self,no,bal):
         self.no=no
         self.bal=bal

    def credit(self,amt):
         self.bal+=amt
         print("RS",amt,"credited")
         print("Total Balance:",self.getbalance())

    def withdraw(self,amt):
         self.bal-=amt
         print("RS",amt,"Deposited")
         print("Total Balance:",self.getbalance())

    def getbalance(self):
         return self.bal


a1=account(101,10000)
a1.credit(1000)                   
        