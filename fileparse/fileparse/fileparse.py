
# file no1: "bee_movie_skript.txt"
# file no2: "gettysburg_adress.txt"

file_name = input("Enter the name of the file to parse: ")

file = open(file_name, "r")
word = input("Enter the word to search for: ")
count = 0

line = file.readline()
while line:
    if word.upper() in line.upper():
        count += line.upper().count(word.upper())
    line = file.readline()

print(f"Searching for {word} in {file_name}...")
print(f"\"{word}\" appears {count} times in {file_name}.")