#checking the number is even or odd
num1=int(input("Enter first Number :"))
num2 = int(input("Enter second Number :"))
num3 = int(input("Enter third Number :"))
if(num1 > num2 and num1 > num3):
    print(num1, "Is the greats Number")
elif(num2 > num1 and num2 > num3):
    print(num2, "is greatest number")
else:
    print(num3, "is greatest number")
    print("Odd Number")