
# to performe read and write operation,( in r+ mode the things get over write)

f = open ("demo.txt", "r+")
f.write ("abc")
print(f.read())
f.close()