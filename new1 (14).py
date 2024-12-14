# to get the count of even number from a file

with open( "abc.txt","r") as f:
    
    data =f.read()
    print(data)
    
    #num = ""
    #for i in range(len(data)):
     #   if(data[i] == ","):
      #      print(int(num)) 
       #     num = ""
        #else:
         #   num += data[i]
    count = 0        
    num = data.split(",")
    for val in num:
        if (int(val) % 2 == 0):
            count +=1
print(count)        