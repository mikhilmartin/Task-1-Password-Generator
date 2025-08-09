import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_pwd():
    pwd_length = int(input("What is the required length of your password? "))
    
    random.shuffle(characters)

    password=[]

    for x in range(pwd_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)
    print(password)

ch = input("Do you want to create a Password (Yes/No)? ")

if ch == "Yes":
    generate_pwd()
elif ch == "No":
    print("Program ended")
    quit()
else:
    print("Invalid Input! Please Input Yes or No")
    quit()