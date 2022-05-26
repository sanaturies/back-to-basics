
import random
head=0
tail=0
for i in range(100):
    r=random.randint(0,1)
    if r:
        head+=1
    else:
        tail+=1
print('num of heads=',head)
print('num of tails=',tail)
print('number of heads away from 50:',-50+head)
print('number of tailss away from 50:',-50+tail)