"""
3 2
1 5 3
3 1
5 7
"""

i_arr,a_arr,b_arr = [input().split() for _ in range(4)][1:]
a_arr,b_arr = set(a_arr),set(b_arr)
print(sum([(i in a_arr) - (i in b_arr) for i in i_arr]))
