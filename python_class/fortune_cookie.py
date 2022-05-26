
# generates random fortunes
import random
adjectives=['amazing','bad','smelly','good','successful','great','awful']
noun=['mirror','house','bag','book','code','school','marker','plant']
verb=['work','break','give','complain','boil','regret','afford','lie']
a=random.choice(adjectives)
n=random.choice(noun)
v=random.choice(verb)
print('tonight you will',v,a,n)