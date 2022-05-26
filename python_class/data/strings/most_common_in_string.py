
# given two strings return the two strings with the letters most in common
# spectrum clustering/measure of similarity
a='sana murthy'
b='advik murthy'
c='neetu hebbal'
d='priya hebbal'
i=354
print(i//10)
names=[a,b,c,d]
difference=[]
num=len(names)**2
to_append=[' ']*num
difference.append(to_append)
print(difference)
iteration=-1
for i in names:
    for j in names:
        iteration+=1
        if i!=j:
            for k in i:
                if k not in j:
                    ' 'in difference
print(difference)