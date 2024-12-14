# find the word in string

def check_word():
    word = "abc"
    count = 1
    data = True

    with open("pratice.txt", "r") as f:
        while data:
            data = f.readline()
            if( word in data ):
                print(count)
                return
            count +=  1
            
    return -1

print(check_word())