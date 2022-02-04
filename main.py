"""print('\n??Mitä ihmettä??')
haaveilija = "Lunta, lunta, lunta"
haaveilija += ". Uriah heep"
print(haaveilija)

# kommentti vain
# toinen kommentti vain hyvä se on

calc_to_unit = 2
print(calc_to_unit)
calc_to_unit -= 1
calc_to_unit += 10

user_input = input()
if user_input.isnumeric():
    print("Numeroita tuli, kiitos")

# Mainos lopussa.
# Tämä mainos tulee Visual Studio Codesta
# Ja tämä
# 01.02.2022
# 01.02.2022 / 2

my_list = ["00", "10", "20", "30", "40", "50"]
print(my_list)

import os
from random import random

print(os.name)

print('*' * 20)

ika = int(input('anna ikä '))
ika += 1
print(f"\nensivuonna ikä on {ika + 1}")

print('x' * 5)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[1][2] = 20
print(matrix[1][2])

a = [5, 2, 1, 7, 4]
print(a)
a.pop()
print(a)
a.append('Nisse-2022')
print(a)
"""

f = open("demofile.txt", "r")
print(f.read())
f.close()
f = open("demofile.txt", "a")
f.write("Kiitos ja näkemiin...")
f.close