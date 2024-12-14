# write a recursive function to calculate the sum of n natural numbers

def sum(n):
    if( n == 0 or n == 1):
        return 1
    else:
        return n + sum(n-1)
    
number = int(input("Enter a number to get the sum is :"))
print(sum(number))