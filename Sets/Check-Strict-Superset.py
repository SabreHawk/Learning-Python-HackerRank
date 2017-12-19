s =set(input().split())
t= set()
for _ in range(int(input())):
    t|=set(input().split())
print(len(t-s)<=0)