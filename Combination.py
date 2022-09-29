from itertools import permutations
n=(input("ENTER THE NUMBER---> "))
p=permutations(n)
for i in list(p):
    print(i)
