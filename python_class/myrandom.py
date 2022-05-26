
'''import random
r=random.randint(1,6)
print(r)'''

# Import the “random” library
# to give you access to random functions
import random
die1 = random.randint(1,9)
print("Random number:", die1)


#random number guesser
difficulty=input("what difficulty level would you like? (easy, medium, hard)")
easy=10
medium=50
hard=100
if difficulty=="easy":
    goal=random.randint(1,easy)
    print("the upper limit is",easy)
elif difficulty=='medium':
    goal=random.randint(1,medium)
    print("the upper limit is",medium)
else:
    goal=random.randint(1,hard)
    print("the upper limit is",hard)
print(goal)
guess=int(input('what is your first guess?'))
if guess==goal:
    print("You won first try!")
elif guess<goal:
    print("guess higher!")
else:
    print("guess lower!")
if guess!=goal:
    guess=int(input('what is your first guess?'))
    if guess==goal:
        print("You won!")
    elif guess<goal:
        print("guess higher!")
    else:
        print("guess lower!")
    if guess!=goal:
        guess=int(input('what is your first guess?'))
        if guess==goal:
            print("You won!")
        else:
            print("sorry, you lost.")
            print('the number was:',goal)
