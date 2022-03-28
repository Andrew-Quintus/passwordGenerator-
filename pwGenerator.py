#Creating a password generator!
import random

print(' Password Generator \n ==================')

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*().,?/"[]=+'

number = input('How many passwords do you want?: ')
number = int(number)

length = input('Input the length of the password(s) you want: ')
length = int(length)
print('Passwords!: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)