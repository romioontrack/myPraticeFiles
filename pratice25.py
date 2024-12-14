# write a recursive function to print the all element of a list

def list(city, index = 0 ):
    if (index == len(city)):
        return
    print(city[index], end = " ")
    list(city, index+1)
    
city = ["tata", "jamshedpur", "ranchi", "patna", "delhi"]
list(city)