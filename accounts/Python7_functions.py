# Keyword def marks the start of function header.
# A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
# Parameters (arguments) through which we pass values to a function. They are optional.
# A colon (:) to mark the end of function header.
# Optional documentation string (docstring) to describe what the function does.
# One or more valid python statements that make up the function body. Statements must have same indentation level (usually 4 spaces).
# An optional return statement to return a value from the function.

#function have reusability code for same task and different inputs. Its define with def keyword
def function1(a, b):
    print("Hello you are in function1", a+b)
function1(5,7)

# average with function
def function2(a,b):
    """This is function which calculate average  (This is called doc string)"""
    average = (a+b)/2
    #print(average)
    return average      # if we want to return value in variable, use return keyword than store in variable and print
av = function2(5,6)
print(av)
print(function2.__doc__)    # doc string is the The first string after the function header and is short for documentation string.




def Foo(x):
  if (x==1):
    return 1
  else:
    return x+Foo(x-1)
print(Foo(4))
