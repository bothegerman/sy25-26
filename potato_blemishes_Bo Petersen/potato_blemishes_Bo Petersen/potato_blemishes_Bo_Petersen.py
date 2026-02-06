
print("Welcome back, Farmer!")
print("1. Grade a potato based on weight")
print("2. Calculate total and average blemishes for 5 potatoes")
print("3. Calculate percentage of perfect potatoes in a batch")
print("")
g = int(input("Please choose your menu option: "))
print("")

# Code assignment no 1
if g == 1:
    weight = int(input("Enter weight of potato: "))
    if weight < 100:
        grade = "small"
    elif weight <= 200:
        grade = "medium"
    else:
        grade = "large"
    print(f"This potato is a {grade} potato.")

# Code assignment no 2
elif g == 2:
    blemish_counts = []
    for i in range(5):
        nr = int(input("Enter the number of blemishes for potato: "))
        blemish_counts.append(nr)
    total = sum(blemish_counts)
    average = total / 5
    print(f"Total blemishes: ", total)
    print(f"Average blemishes per potato:", average)

# Code assignment no 3
elif g == 3:
    all_potatoes = [0,2,5,1,0,8,3,0]
    perfect_potatoes = []
    for p in all_potatoes:
        if p == 0:
            perfect_potatoes.append(p)
    perfect = len(perfect_potatoes)
    total = len(all_potatoes)
    percentage = (perfect / total) * 100
    print(f"Number of perfect potatoes: {perfect}")

else: 
     print("Invalid menu option. Please start over and choose 1, 2, or 3.")







