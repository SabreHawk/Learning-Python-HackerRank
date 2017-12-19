
def average(array):
    # your code goes here
    temp_set = set(array)
    return sum(temp_set)/len(temp_set)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)