import random

#take the value of n
n=int(input("Enter n: "))
while n<=0:
    n=int(input("Enter a positive integer for n: "))
    # if n is enter as negative number, it would ask it enter a positive number. 
print("Welcome to Guess My Number!")
print("Please think of a number between 0 and %d"%(n))
#setting the guessing number 
lower_bound=0
upper_bound=n
while True:
    #generate a random number
    guess_num=random.randint(lower_bound,upper_bound)
    print("Is yout number: %d?"%(guess_num))
    print("Please enter C for correct, H for too high, or L for too low.")
    exit=0
    while True:
        guess_number=input("Enter your response(H/L/C): ")
        if guess_number=="H":
            upper_bound=guess_num-1
            break
        elif guess_number=="L":
            lower_bound=guess_num+1
            break
        elif guess_number=="C":
            exit=1
            break
    if exit==1:
        break
print("Thank you for playing Guess My Number!") 
