
# Word Jumble is a game where a random word is jumbled up and the user tries to unscramble it.
import random
word_chocies=['sharpie','binder','handbag','mississippi','gamble','unscramble']
word=random.choice(word_chocies)
correct=word
scramble=''
guess=''
#print(word)   this was for testing
while word:
    r=random.randint(0,len(word)-1)
    scramble+=word[r]
    word=word.replace(word[r],'')
   
print(scramble)

while guess!=correct:
    guess=input('what do you think the unscrambled word is? (enter 0 to quit) ')
    if guess=='0':
        print('the word was',correct)
        break 
    elif guess!=correct:
        print('Wrong! try again.')
    else:
        print('Correct!')


