# Faulty Calculator
# 45* 3 = 555, 56+9=77, 56/6= 4

num1 = int(input("Enter first Number "))
num2 = input("Chose + - * / ")
num3 = int(input("Enter secound Number "))

if num1 == 45 and num2 == "*" and num3 == 3:
    print(555)
elif num1 == 56 and num2 == "+" and num3 == 9:
    print(77)
elif num1 == 56 and num2 == "/" and num3 == 6:
    print(4)
elif num2 == "+" :
    plus = num1 + num3
    print(plus)
elif num2 == "-":
    min = num1 - num3
    print(min)
elif num2 == "*":
    mul = num1 * num3
    print(mul)
else:
    div = num1 / num3
    print(format(div, '2f'))