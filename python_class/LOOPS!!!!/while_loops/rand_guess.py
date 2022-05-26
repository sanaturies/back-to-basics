
'''import random
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
    print("guess lower!")'''


import random
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
     
while guess!=goal:
    if guess<goal:
        if guess<=0:
            break
        print('guess lower')
        guess=int(input('what is your first guess?'))
    else:
        print("guess higer")
        guess=int(input('what is your first guess?'))
if guess<=0:
    print('the number was',goal)
    print('thanks for playing')
            
else:
    print('congradulations for guessing correctly')
    print("thanks for playing!")
    