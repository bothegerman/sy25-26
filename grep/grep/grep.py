import glob

# name of the file: "words.txt"
files = glob.glob("*.txt")

#filename = input("Enter the filename: ")
#filename = "words.txt"


while True:
    pattern = input("Enter the search string: ")
    if pattern == "" or pattern == "break":
        break

    for filename in files:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for i, line in enumerate(lines):
            if pattern in line:
                print(filename, i+1, line.strip())

