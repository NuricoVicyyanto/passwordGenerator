# import modules
import random
import string

print("Welcome to the Password Generator!")

# input length of password
length = int(input("How long would you like your password to be? "))

# define character sets
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
special = string.punctuation

# combine character sets
create_password = lower + upper + numbers + special

# use random.sample to select characters from create_password
temp_password = random.sample(create_password, length)

# create password
password = ''.join(temp_password)

#print password
print("Your password is: " + password)