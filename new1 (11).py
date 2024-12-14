# To search a charater in string using file handling

with open ("pratice.txt", "r") as f:
    content = f.read()
    if(content.find("learning") != -1):
        print("found")
        
    else:
        print(" Not Found")
        