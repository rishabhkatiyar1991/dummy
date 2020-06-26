# Astrologer's Stars (Pattern Printing)
stars = int(input("Enter Number "))
print("Enter the Number for boolan value 1 OR 0 ")
bol = int(input())
val = bool(bol)
if val == True:
    for i in range(1,stars+1):
        for j in range(i):
            print("*", end=" ")
        print("")
elif val== False:
    for k in range(stars,0,-1):
        for l in range(1,k+1):
            print("*", end=" ")
        print("")
