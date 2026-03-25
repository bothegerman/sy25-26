
import sys
from wsgiref import headers
# password: "todesgeil"
# ai version
with open("password.txt", "r") as f:  
    password = f.read()  


attempt = 0
while True:
    if attempt < 3:
        user_input = input("Enter password: ")  
    if user_input == password:  
        print("Access granted!\n") 
        break
    elif user_input != password and attempt < 3:  
        print(f"Incorrect. [{2 - attempt} left]")  
        attempt += 1
    else:
        print("Too many failed attempts. Access denied.\n")
        sys.exit()


print(" Good Day!\n Choose an application: ")
print("[1] Expenses   [2] Passwords   [3] Exit\n")
app = input(" ")


with open("expenses.csv", "r") as e:  
    #e.write("total_price,price_per_unit,amount,category,date,note\n")  
    #expenses = e.read()
    lines = e.readlines() 

expenses = []  

keys = lines[0].strip().split(",")  
objects = [line.strip().split(",") for line in lines]
ex_dict = dict(zip(keys, objects))
expenses.append(ex_dict)  
print(expenses)

"""
# wenn fertig dann fuer mehrere benutzer anlegen 
# my version
password_file = open("passwords.txt", "r")
password = password_file.read()
user_input = input("Enter password: ")  
if user_input == password:  
    print("Access granted!")  
else:  
    print("Access denied.") 

"""