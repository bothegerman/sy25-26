
# The initial lineup
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]

# 1. Add the headliner
headliner = ("The Byte Beats", "Synthwave", 90)
lineup.append(headliner)

#2. Remove the first band from the lineup and put them at the end of the lineup
# rb == removed band 
rb = lineup.pop(0)
lineup.append(rb)

# 3. Add a new band to the end of the lineup
lineup.remove[0]

# 4. Print the final lineup


print(lineup)
