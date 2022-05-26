

'''Print the name in the following formats. Below is an example of EXACTLY what the output would be with “John Jeff Smith” entered
Initials: J.J.S.
Initials partial: J.S.
Last then first: Smith, John
Last then first middle: Smith, John Jeff
First M.I. Last: John J. Smith
Nickname / First name repeated: JohnJohn'''

#separateing the full name into separate names
'''fullname='agatha stewart short junior'
lenght=len(fullname)
spaceindex=fullname.find(' ')
spaceindex2=fullname.find(' ',spaceindex+1)
spaceindex3=fullname.find(' ',spaceindex2+1)
first=fullname[0:spaceindex]
middle=fullname[spaceindex+1:spaceindex2]
last=fullname[spaceindex2+1:lenght]'''
fullname='agatha stewart short junior'
names={}
spaceindex=0
num_of_space=fullname.count(' ')
for i in range(num_of_space):
    spaceindex=fullname.find(' ',spaceindex+1)
    names[i]=spaceindex
print(names)

empty=''
dot='.'
prev=names[0]
#initials
for i in range(len(names)):
    v=names[i]
    j=empty+str(fullname[v-prev])
    prev=v
    print(j)

'''#using the names to produce the results
empty=''
dot='.'
#initials
print(empty+first[0]+dot+middle[0]+dot+last[0])
#partial initials
print(empty+first[0]+dot+last[0])
#Last,First
print(last,first)
#last,fist,middle
print(last,first,middle)
#fist middle initial last
print(first,middle[0],last)
#nickname
print(first*2)'''