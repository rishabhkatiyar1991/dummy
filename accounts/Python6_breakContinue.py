#value should greater than 5 and lessthan 45.
"""i=0
while(True):
    if i+1<=5:
        i=i+1
        continue
    print(i+1, end=" ")
    if i==44:
        break
    i=i+1"""

# print some word if no should greater than 100 using user input
"""while(True):
    userno = int(input("Enter a Number\n"))
    if userno > 100:
        print("Congratulation number is greater than 100\n")
        break
    else:
        print("Please Re-enter Number\n")
        continue"""

# no of guesses 9, print no of guesses left, game over, No of guesses he took to finish
n=18
guesses_total_no = 1
print("You have take 9  Attempt")
while(guesses_total_no <= 9):
    guess_no = int(input("Guess the Number "))
    if guess_no < n:
        print("Guesses Number is lesser number to actul number ")
    elif guess_no > n:
        print("Guesses number is greater than actul number ")
    else:
        print("congrates to chosses right nunber!!!")
        print("Number of guesses he took to finish:  ", guesses_total_no)
        break
    print("Number of guesses left: ", 9 - guesses_total_no)
    guesses_total_no += 1
if guesses_total_no > 9:
    print("Game Over")



