l = 10      # Global
def function_var(n):
    #l = 5        # Local
    m = 8
    #print(b, m) # It's throw error bcoz b not define in global or local side (NameError: name 'b' is not defined)
    global l    # If want to change global var, must use global keyword with-in function than we should change other wise we found error
    l = l+ 45
    print(l, m)
    print(n, "I have printed")

function_var("This is me!!!")
#print(m)        #NameError: name 'm' is not defined



def ris():
    x=20
    def rohan():
        global x     # If use global var than it's jump process and search global variable,
                        # must have to define globaly for main function (ris()) not rohan().
        x=88
    print("before calling rohan() ",x)
    rohan()
    print("after calling rohan() ",x)       #before calling rohan()  20 / after calling rohan()  20
ris()
print(x) # its print 88 bcoz it's out side.