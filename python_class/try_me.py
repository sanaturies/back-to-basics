
# given a lenght and width of a rectangle, show area
lenght=4
width=7
print('lenght=',lenght)
print('width=',width)
print('area=',lenght*width)

# sum of all numbers 1-10
count=0
num=100
for i in range(num+1):
    count+=i
print(count)

#average
average=count/num
print(average)

#sum of n numbers with n*(n+1)/2
num=6
print(num*(num+1)/2)

#sum of n numbers with n*(n+1/2) when adding certain intervals of numbers.
#10,2 => 2+4+6+8+10 => 10/2=5; 5/2=2.5 => 10+2=12 => (10+2)*2.5=30
num=1000000
interval=1
num_of_num=(num/2)/interval
print((num+interval)*num_of_num)

#given a number return lowest possible number that could give n when all the numbers before it are added together.
n=33



