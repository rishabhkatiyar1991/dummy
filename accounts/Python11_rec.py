# n1 = n * n-1 * n-2
# n1 = n * (n-1)!
#numb = int(input("Enter the Number "))
def fun_iterative(n):
    """
        :param n: Integer
        :param: n * n-1 * n-2 .................
    """
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact

def fun_recursive(n):
    if n == 1:
        return 1
    else:
        return n * fun_recursive(n-1)
    # n = 5
    # 5 *  fun_recursive(4)
    # 4 *  fun_recursive(3)
    # 3 *  fun_recursive(2)
    # 2 *  fun_recursive(1)
    # 5*4*3*2*1 = 120


numb = int(input("Enter the Number "))
print("Print Iterative function ",fun_iterative(numb))
print("Print Recursive function ",fun_recursive(numb))



















# def factorial_iterative(n):
#     """
#         :param n: Integer
#         :param: n * n-1 * n-2 .................
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#
#
# def factorial_recursive(n):
#     if n ==1:
#         return 1
#     else:
#         return n *factorial_recursive(n-1)
#     # 5 * factorial_recursive(4)
#     # 4 * factorial_recursive(3)
#     # 3 * factorial_recursive(2)
#     # 2 * factorial_recursive(1)
#     # 5*4*3*2*1= 120
#
# number = int(input("Enter the number"))
# print("Factorial using iterative method ", factorial_iterative(number))
# print("Factorial using Recursive method ", factorial_recursive(number))