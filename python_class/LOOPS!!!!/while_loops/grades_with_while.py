
'''i=1
summed=0
nums=10
while i<=nums:
    grade=int(input('what is your grade?'))
    summed+=grade
    i+=1
print(' \n total of all grades',summed)
print(' \n average of all grades',summed/nums)'''

i=2
summed=0
while i>=0:
    i+=1
    print(i)
    grade=int(input('what is your grade? please enter a negative to quit '))
    if grade<0:
        break
    summed+=grade

print(' \n total of all grades',summed)
print(i-1)
print(' \n average of all grades',summed/(i-2))


