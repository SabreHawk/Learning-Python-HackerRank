if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    temp_list = list(set(arr))
    temp_list.sort()
    print(temp_list[len(temp_list)-2])
