for _ in range(int(input())):
    a,b = [set(input().split()) for __ in range(4)][1::2]
    print(len(a-b) == 0)
        