
#you have a number. computer guesses

maximum=int(input('what the maximum number? '))
minimum=int(input('what is the minimum number? '))
guess=False
while guess==False:
    average=((maximum+1)+minimum-1)//2
    print("my guess is",average,'is it too high, too low, or correct?')
    feedback=input()
    if feedback=='too high':
        maximum=average
    elif feedback=='too low':
        minimum=average
    elif feedback=='correct':
        print('yay I won!')
        guess=True
    else:
        print('please give a valid response: too high, too low, correct')
    