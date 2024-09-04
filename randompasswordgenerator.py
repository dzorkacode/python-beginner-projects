import string
import random

characters=list(string.ascii_letters+string.digits+"!@#$%^&*()_- ")

def generate_password():
    password_length=int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password=[]

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password="".join(password)

    return password

option= input('Do you want to generate a password? (yes/no): ')

if option=="yes":
    print(generate_password())
elif option=="no":
    print('program ended')
    quit()
else:
    print('invalid input, please input yes or no')
    quit()