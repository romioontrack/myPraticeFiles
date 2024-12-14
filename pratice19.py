# write a function to get the factorial

def factorial(n):
    sum=1
    for i in range(n):
        sum +=sum * i
    return sum

number = int(input("Enter a number to get the factorial of a number :"))
pic = factorial(number)
print(pic)