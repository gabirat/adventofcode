def rule1(n):
    stringified = str(n)
    for i in range(0, len(stringified) - 1):
        if stringified[i] == stringified[i+1]:
            return True
    return False

def rule2(n):
    stringified = str(n)
    for i in range(0, len(stringified) - 1):
        if int(stringified[i+1]) < int(stringified[i]):
            return False
    return True

possibilities = 0

for num in range(245182, 790572):
    if rule1(num) and rule2(num):
        possibilities += 1

print(possibilities)