import random
length = int(input("Please enter your password length: "))
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"
symbol = "[{()}]!@#$%&/"
total = lower + upper + digit + symbol
password = "".join(random.sample(total,length))
print("\nYour password is: ",password)