import random

rndrange = random.randrange(1001,10001,2)
print(rndrange)
rnint = random.randint(1001,10001)
print(rnint)
"""The only difference that I know between randrange and randint is that randrange([start], stop[, step]) you can use the step and random. 
randrange(0, 1) will not consider the last item, while randint(0, 1) returns a choice inclusive of the last item."""