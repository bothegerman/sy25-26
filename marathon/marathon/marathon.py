
runner_info = ("Chris", 540, 54)
mile_splits = [8.5, 8.2, 8.4]

mile_splits.append(8.3) 
print(mile_splits)


total_time = 0
total_miles = 0
for i in mile_splits:
    print(i)
    total_miles += 1
    total_time += i
print(f"Total Time: {total_time}, Total miles: {total_miles}")


"""
total_time = sum(mile_splits)
average_pace = total_time / len(mile_splits)
print(f"Runner: {runner_info[0]}")
print(f"Total Time: {total_time} minutes")
print(f"Average Pace: {average_pace} minutes per mile")

"""