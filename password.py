import random
import string
print('*****************password generator*********************')

len=int(input("enter length of password: "))

choice = string.ascii_letters + string.digits + string.punctuation

password = ""   

for i in range(len):
    password = password + random.choice(choice)

print(f"Password generated: {password}")
