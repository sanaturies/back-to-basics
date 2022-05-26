
# print letters in range 
string=input('word? ')
flag=True
while flag==True:
    lenght=len(string)
    a=input('number? ')
    b=input('number? ')
    if a.isdigit==False or b.isdigit==False:
        print('please enter only numbers')
    a=float(a)
    b=float(b)
    if a<0 or b<0:
        print('please provide a positive number')
    elif a>lenght or b>lenght:
        print('please provide a number less than or equal to',lenght)
    elif a>b:
        x=b
        b=int(a//1)
        a=int(x//1)
        r=string[a:b+1]
        print(r[::-1])
        flag=False
    else:
        flag=False
a=int(a//1)
b=int(b//1)
print(string[a:b+1])
