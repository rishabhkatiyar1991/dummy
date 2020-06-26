print("Enter first no")
no1 = input()
print("Enter second no")
no2 = input()
try:        # It's user for Exception handling, it's use for your code should run when error occour
    num = int(no1)+int(no2)
    print(num)
except Exception as e:
    print(e)

print("This line is most important")