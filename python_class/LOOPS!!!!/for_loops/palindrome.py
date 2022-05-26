
pal="radar"
print("forward=",pal)
print('backwards=',end=' ')
bkw=''
for i in range(len(pal)-1,-1,-1):
    print(''+pal[i], end='')
    bkw+=pal[i]
print('\n',bkw)
if pal==bkw:
    print("\nit is a PALINDROME!\n")

else:
    print("\nit is not a PALINDROME!\n")

#extension
pal="cat"
print("forward=",pal)
print('backwards=', pal[::-1])
bkw=''
for i in range(len(pal)-1,-1,-1):
    if ' 'in pal:
        pal=pal.replace(' ','')
        print(pal)
for i in range(len(pal)-1,-1,-1):
    print(''+pal[i], end='')
    bkw+=pal[i]
print('\n',bkw)
pal=pal.lower()
bkw=bkw.lower()
if pal==bkw:
    print("\nit is a PALINDROME!")

else:
    print("\nit is not a PALINDROME!")