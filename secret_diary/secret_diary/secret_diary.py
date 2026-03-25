
import datetime

while True:
    choice = int(input("What would you like to do? \n1. Read the diary \n2. Write in the diary \n3. Clear diary \n4. Exit \n"))
    if choice == 1:
        file = open("my_diary.txt", "r")
        line = file.read()
        print("")
        print("Your diary entries:")
        print(line)
        print("")
        file.close()
    elif choice == 4:
        break