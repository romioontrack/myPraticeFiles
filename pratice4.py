#wap to check the entered number is plindrom or not
list1 = [1,2,3,1]
#list2 = []

list1_copy = list1.copy()
list1_copy.reverse()

if(list1 == list1_copy):
    print("plindrom")
else:
    print("Not Plindrom")


