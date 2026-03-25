#open file "output.txt" in - desktop; github; sy25-26; files; output.txt - to see text adn changes 

file_name = "output.txt" #creates file

file = open(file_name, "a")   # with "w" it writes the file new, with "a" it opens the file and just appends the code
for i in range(10):
    file.write(f"{i} Hello, World!\n")   # writes a "hello world" in every new line of loop

file.close()


file = open(file_name, "r")  # opens file to read only
for line in file:
    print(line)
#line = file.readline()
print(line)
