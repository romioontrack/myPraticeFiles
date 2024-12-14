#factorial of a number

sum = 1
#index =1
number  = int(input("Enter a number to get the factorial :"))
for i in range(1, number+1):
    sum *= i

print(" The factorial iof a number is :", sum )
