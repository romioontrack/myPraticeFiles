class Account:
    def __init__(self,bal,acc):
        self.account_number= acc
        self.balance =bal
        
        #the amount debited from account
    def debit(self,amount):
        self.balance -= amount
        print("Rs .",amount, "Sucessfully debited")
        print("Total Balance is :",self.available_bal())
        

#the amount credited to the balance    
    def credit(self,amount):
        self.balance += amount
        print("Rs .",amount, "Sucessfully credited")
        print("Total Balance is :",self.available_bal())  
        
    def available_bal(self):
        return self.balance  
        
        
s1 = Account(10000000000, 33113005735)
s1.debit(1000)
s1.credit(20000)
s1.credit(500000)