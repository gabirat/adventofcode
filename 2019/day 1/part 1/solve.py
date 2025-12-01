with open("input.txt", "r") as file:
	data = file.read().splitlines()

suma = 0

for d in data:
	suma += int(d) // 3 - 2

print(suma)