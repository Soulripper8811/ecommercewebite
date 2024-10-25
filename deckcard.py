import itertools,random

deck=list(itertools.product(range(1,14),["spade","heart","diamond","club"]))

random.shuffle(deck)

print("You got")
for i in range(10):
    print(deck[i][0], "of",deck[i][1])
