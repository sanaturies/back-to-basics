
# Print the numbers 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
# 1+3=4, 4+5=9, 9+7, 16+9=25, 25+11=36

# way 1
i=0
summed=0
while summed <=100:
    if i%2!=0:
        summed+=i
        print(summed)
    i+=1

# way 2
i=1
summed=0
while summed <100:
    summed+=i
    print(summed)
    i+=2

# way 3
i=1
square=0
while square <100:
    square=i**2
    i+=1
    print(square)

