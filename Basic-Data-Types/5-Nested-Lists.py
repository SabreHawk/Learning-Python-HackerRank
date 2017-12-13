import operator
if __name__ == '__main__':
    markSheet = []
    nameSheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        markSheet.append([name,score])
    markSheet.sort(key = operator.itemgetter(1))
    sec_score = markSheet[1][1]
    for i in range(len(markSheet)):
        if markSheet[i][1] == sec_score:
            nameSheet.append(markSheet[i][0])
    nameSheet.sort()
    for _ in range(len(nameSheet))
        print(nameSheet[_])