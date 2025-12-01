with open("input.txt", "r") as file:
	data = file.read().splitlines()

suma = 0

def calcFuel(mass):
	fuel = mass // 3 - 2
	if (fuel // 3 - 2) <= 0:
		return fuel
	else:
		return fuel + calcFuel(fuel)

for val in data:
	suma += calcFuel(int(val))

print(suma)