k,s = int(input()),list(map(int,input().split()))
print((sum(set(s))*k- sum(s))//(k-1))