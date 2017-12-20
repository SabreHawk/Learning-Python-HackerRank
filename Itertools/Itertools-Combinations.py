import itertools 
a, b = input().split()
for l in range(1,int(b)+1):
    [print("".join(i)) for i in itertools.combinations(sorted(a), l)]