
from asyncio.windows_events import NULL


total = 0
num = int(input("Please enter a number (0 to stop)"))
large=num
small=num
while num != 0 :
    if num>large:
        large=num
    else:
        small=num
        
    #Each time they enter a number, display whether it is positive or negative.
    if num > 0:
        print("The number is positive", end=" ") # the end=" " makes it so that the next print statement is printed on the same line as this one. So instead of ending in a \n it ends in a space.
    else:
        print("The number is negative", end=" ")

    #Each time they enter a number, display whether it is even or odd.
    if num%2 == 0:
        print(" and even")
    else:
        print(" and odd")

    total = total + num
    num = int(input("Please enter a number (0 to stop)"))
    
print("The sum is:", total) 
print("the smallest number entered is:",small)
print("the largest number entered is:", large)
# What if we want to calculate the average?

g=6
if g==6:
    pass
else:
    print('oop')
