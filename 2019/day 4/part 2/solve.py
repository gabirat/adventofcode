# def rule1(n):
#     stringified = str(n)
#     for i in range(0, len(stringified) - 1):
#         if stringified[i] == stringified[i+1]:
#             return True
#     return False

def rule2(n):
    stringified = str(n)
    for i in range(0, len(stringified) - 1):
        if int(stringified[i+1]) < int(stringified[i]):
            return False
    return True

def rule1(n):
    stringified = str(n)
    ranking = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
    }
    for d in stringified:
        ranking[d] += 1
    for r in ranking:
        if ranking[r] == 2:
            return True
    return False

possibilities = 0

for num in range(245182, 790572):
    if rule1(num) and rule2(num):
        possibilities += 1

print(possibilities)