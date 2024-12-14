# replace a word in file handling
with open ("pratice.txt", "r") as f:
    content = f.read()
    
new_data = content.replace("Java", "Python")
print(new_data)

with open ("pratice.txt", "w") as f:
    f.write(new_data)