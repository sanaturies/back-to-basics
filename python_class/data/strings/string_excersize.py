
# using replace method
string='life is great'
string=string.replace('great', 'pointless')
print(string)

#print certain parts.
string='When you love your team, you never stop wondering what they\'re doing.'
print(string[0])
print(string[0:10])
print(string[-1])
print(string[-44:-1])

#string operaters
string='but no one could argue that a fillet o fish could exist without it\'s perfectly steamed buns'
print('imagine' in string) #returns true
print('imperfect' in string) #returns false
print('hogwarts' not in string) #returns false
print('castel' not in string) #returns true

#string conversions
string='''My tea's gone cold I'm wondering why I
Got out of bed at all
The morning rain clouds up my window
And I can't see at all
And even if I could it'll all be gray
Put your picture on my wall
It reminds me, that it's not so bad
It's not so bad'''
print(string.capitalize())
print(string.lower())
print(string.upper())
print(string.swapcase())
print(string.title())
print(string.count('a'))
print(string.count('a',0,10))

#string comparisons
string='''Meat-eating orchids forgive no one just yet
Cut myself on angel hair and baby's breath
Broken hymen of Your Highness, I'm left black
Throw down your umbilical noose so I can climb right back'''
print(string.islower())
print(string.isupper())

#string-searching
string='''And the sky was all violet
I want it again, but violent, more violent
Yeah, I'm the one with no soul
One above and one below'''
sub='violet'
print(string.find(sub))
print(string.find(sub,9)) # 9 is the index at which python starts searching
print(string.find(sub,0,20))# 20 is the index at which python stops searching.
print(string.rfind(sub)) 

# Try Me
# Given a string with a first and last name,break it up in seperate variables for the first and last name.

# way 1
fullname=input('full name?')
firstname=fullname[0:4]
lastname=fullname[5:11]
print(fullname,'\n',firstname,'\n',lastname)

# way 2
space_index=fullname.find(' ')
lenght=len(fullname)
firstname=fullname[0:space_index+1]
lastname=(fullname[space_index:lenght])
print(fullname,'\n',firstname,'\n',lastname)

