
lineup = [("The Pythonistas", "Rock", 45),
    ("Code Play", "Indie", 30),
    ("Syntax Error", "Metal", 60)]

def print_lineup(bands):
    total_time = sum[time]
    print("Current Lineup: {lineup}")
    print("Total Festival Duration: {total_time} minutes")

def add_band(bands):
    name = input("Enter band name: ")
    genre = input("Enter band genre: ")
    time = int(input("Enter performance time (in minutes): "))
    lineup.append((name, genre, time))
    print(f"Added {name} with a performance time of {time} minutes.")



# start
print("\n--- Py-Fest 2026 Stage Manager ---")
print("1. View Lineup and Total Time")
print("2. Add a New Band")
print("3. Move First Band to End (Late Arrival)")
print("4. Remove a Band by Name")
print("5. Move Band to Specific Position")
print("6. Exit")
choice = int(input("Select an option (1-6): "))

if choice == 1:
    print_lineup(bands)

elif choice == 2:
    add_band(bands)

elif choice == 3:
elif choice == 4:
elif choice == 5:

elif choice == 6:
    print("Exiting Py-Fest 2026 Stage Manager. Goodbye!")
