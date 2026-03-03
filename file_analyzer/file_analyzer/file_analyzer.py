
import glob

error_list = []
error_count = 0

warn_list = []
warn_count = 0

ok_list = []
ok_count = 0

# Get all .txt files in the directory

file_list = glob.glob("server_dump/*.txt") 


for file in file_list:
    datei = open(file, "r")
    line = datei.readline()
    if "ERROR" in line:
        error_count += 1
        error_list.append(file)
    elif "WARN" in line:
        warn_count += 1
        warn_list.append(file)
    elif "OK" in line:
        ok_count += 1
        ok_list.append(file)

    datei.close()

print("Error count:", error_count)
print("File names:", error_list)
print("")
print("Warn count:", warn_count)
print("File names:", warn_list)
print("")
print("OK count:", ok_count)
print("File names:", ok_list)

print("Total files analyzed:", len(file_list))