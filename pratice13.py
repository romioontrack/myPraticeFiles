

num = (1,4,9,16,25,36,49,64,81,100)
x=100
indx=0

for ch in num:
    print("searching")
    if(ch == x or indx == 4):
        print("found the element or reach the maximum limit :",indx)
        break
    indx += 1
    

