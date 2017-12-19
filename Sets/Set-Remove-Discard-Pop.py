n,s = int(input()),set(map(int, input().split())) 
for _ in range(int(input())):
    cmd_list = input().split()
    if cmd_list[0] == 'pop':
        s.pop()
    elif cmd_list[0] == 'remove':
        s.remove(int(cmd_list[1]))
    elif cmd_list[0] == 'discard':
        s.discard(int(cmd_list[1]))

print(sum(s))
    