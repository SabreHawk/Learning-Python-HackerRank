e_index,f_index = [set(input().split()) for _ in range(4)][1::2]
print(len(e_index ^ f_index))