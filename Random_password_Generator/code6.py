#Random Password Generator:

import random
import string

var1=list(string.ascii_letters)
var2=list(string.digits)
var3=list(string.punctuation)

pass_len=12
total_char=var1+var2+var3
password=""

for i in range(pass_len):
    password+=random.choice(total_char)

print(f"\nYour new generated password is: {password}")