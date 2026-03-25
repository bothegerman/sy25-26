
A2 = ["A2", ("Ford", "Focus", "WRC"), 224, (221, 300), 5400, 5.5, 1995, 4]

B1 = ["B1", ("Seat", "Cordoba", "WRC"), 230, (221, 300), 6000, 5.0, 1998, 4]

C1 = ["C1", ("Subaru", "Impreza", "WRC"), 220, (221, 300), 5500, 5.4, 1994, 4]
C2 = ["C2", ("Opel", "Astra", "GSi"), 235, (235, 320), 6200, 5.6, 2962, 6]
C3 = ["C3", ("VW", "Polo", "GTi"), 185, (96, 103), 7600, 8.0, 1600, 4]

D2 = ["D2", ("Toyota", "Celia", "GT-Four"), 245, (220, 299), 5600, 5.3, 1998, 4]
D3 = ["D3", ("Seat", "Toledo", "Marathon"), 220, (195,330), 8400, 5.2, 2100, 5]
D4 = ["D4", ("Peugot", "206", "WRC"), 225, (221,300), 5600, 5.4, 1996, 4]

E1 = ["E1", ("Mitsubishi", "Carisma", "GT"), 225, (213, 290), 6000, 5.2, 1996, 4]
E3 = ["E3", ("Skoda", "Octavia", "WRC"), 230, (221, 300), 7500, 5.3, 2000, 4]
E4 = ["E4", ("Austin", "Metro", "6"), 240, (265, 360), 9800, 3.4, 3600, 6]

F1 = ["F1", ("VW Off-road", "Bug", " "), 185, (104,142), 6000, 9.0, 1880, 4]
F2 = ["F2", ("Mitsubishi", "Galant"," "), 180, (216, 294), 5800, 6.3, 3395, 4]
F3 = ["F3", ("Renault", "Megane", " "), 218, (198, 270), 8400, 5.9, 1995, 4]

G1 = ["G1", ("Citroen", "Visa", "4x4"), 190, (74, 100), 7680, 9.0, 1566, 4]
G2 = ["G2", ("Seat", "Ibiza", "GTi"), 220, (205, 280), 8400, 6.5, 1984, 4]
G3 = ["G3", ("Mitsubishi", "Pajero", " "), 185, (153, 208), 7000, 9.6, 3497, 6]

end = (" ",("end"," "," "))

cars = [A2, B1, C1, C2, C3, D2, D3, D4, E1, E3, E4, F1, F2, F3, G1, G2, G3, end]

def print_car(c):
    print("")
    print(f" |   {c[0]}   {c[1][0]} {c[1][1]} {c[1][2]}       |")
    print(" |                                 |")
    print(" |        \_______________/        |")
    print(" |        __/_|______|__\__        |")
    print(" |        /OO___________OO\\        |")
    print(f" |         |_/___{c[0][0]}-{c[0][1]}___\_|         |")
    print(" |        \@@__|_|_|_|__@@/        |")
    print(" |                                 |")
    print(f" | Top Speed:  {c[2]} | 0-60:  {c[5]}    |")
    print(f" | KWh/HP: {c[3][0]}/{c[3][1]} | Cubic cm: {c[6]}|")
    print(f" | RPM:   {c[4]}     | Cylinder: {c[7]}   |")
    print(" |                                 |")
    print("")

"""
for c in cars:
    print_car(c)
"""

i = 1

print("")
for c in cars:
    print(" ", i, c[1][0], c[1][1], c[1][2])
    i += 1
print("")

choice = 0
while True:
    choice = int(input("Enter # of the car you want to choose: "))
    if choice == 18:
        break
    choice -= 1
    print_car(cars[choice])