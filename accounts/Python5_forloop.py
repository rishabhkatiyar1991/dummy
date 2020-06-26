items = [int, float, "rishabh", 5,7,10,4,23,22,7,19,18,6]
for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item)
