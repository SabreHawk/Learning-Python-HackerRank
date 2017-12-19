m_arr,n_arr = [set(input().split()) for _ in range(4)][1::2]
print("\n".join(sorted(m_arr^n_arr,key = int)))