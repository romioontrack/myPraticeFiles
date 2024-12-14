#create a class Order which store item & its price. 
# Use dunder function __gt__() to convey that: order1> order2 if price of Order1> price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self,order2):       # __gt__ use to compare the price in dunder function
        return self.price > order2.price
    
order1 = Order("chips", 20)
order2 = Order("tea",18)

print(order1 > order2) # True