# Professional way of wiriting the file handling syntex

with open ("demo.txt", "r") as f:
    content = f.read()
    print(content,"\n")
    f.close()
    
    # By using with file its autometically close file after print no need to close it
    
with open("demo.txt", "w") as f:
    f.write("The new data")
    