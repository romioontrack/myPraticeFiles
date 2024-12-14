# To generate the random pass word by using list inheretance

import random
import string

pass_len = 12
value = string.ascii_letters + string.digits + string.punctuation

password = ""
#for i in range (pass_len):
 #   password += random.choice(value)
    
#print("Your Password is :", password)

# list comprehension function for i in range (n)
res = "".join([random.choice(value) for i in range(pass_len)])
print(res)