
'''Print the name in the following formats. Below is an example of EXACTLY what the output would be with “John Jeff Smith” entered​
Initials: J.J.S.
Initials partial: J.S.
Last then first: Smith, John
Last then first middle: Smith, John Jeff
First M.I. Last: John J. Smith
Nickname : First name repeated: JohnJohn'''

# finding intials
fullname='sana guru murthy'
spaceindex=fullname.find(' ')
spaceindex2=fullname.find(' ',spaceindex+1,-1)
print(fullname[0],fullname[spaceindex+1],fullname[spaceindex2+1])

#finding intials automated
fullname='Sana guru Murthy'
initial=''
initial+=fullname[0]
initial+='.'
for i in range(len(fullname)):
    if fullname[i]==' ':
        initial+=fullname[i+1]
        initial+='.'
print(initial.upper())

# Last then first
fullname='sana guru murthy'
lenght=len(fullname)
spaceindex=fullname.find(' ')
spaceindex2=fullname.find(' ',spaceindex+1)
spaceindex3=fullname.find(' ',spaceindex2+1)
first=fullname[0:spaceindex]
middle=fullname[spaceindex+1:spaceindex2]
last=fullname[spaceindex2+1:lenght]
print(last,first)
# last first middle
print(last,first,middle)

# First Middle Initial Last
print(first,middle[0],last)

#Nickname
print(first*2)



