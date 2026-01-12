def print_lineup(bands):
    total_time = sum
    print("Current Lineup: {lineup}")

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
