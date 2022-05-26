
#take any english word and turn it in pig latin.
word=input('word? ')
word=word.split()
print(word)
vowel=['a','e','i','o','u']
for i in range(len(word)):
    a=word[i][0]
    if a not in vowel:
        word[i]=word[i].replace(a,'')
        word[i]+=a
        word[i]+='ay'
    else:
        word[i]+='yay'
print(word)