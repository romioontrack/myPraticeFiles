# recursion ; repeatingly call function itself or recursive function

def show(n):
    if(n == 0): # Base Case(Which decide to stop the function)
        return
    print(n, "\n" )
    show(n-1)
    print("End")
    
num = int(input("Enter a number :"))
show(num)