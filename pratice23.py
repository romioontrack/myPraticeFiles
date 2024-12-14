# get the factorial of a  number using recursion

def fac(n):
    if (n == 1 or n == 0):
        return 1
    
    elif(n < 0):
        print("Enter the value greater than 1 :")
        return
    
    else :
        return  n * fac(n-1)
    
num = int(input("Enter a number to get the factorial of a number :"))

fact = fac(num)
print(fact)