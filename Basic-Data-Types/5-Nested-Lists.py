solution = 1
if solution == 1:
    a = [[input(), float(input())] for i in range(int(input()))]
    s = sorted(set([x[1] for x in a]))
    for name in sorted(x[0] for x in a if x[1] == s[1]):
        print (name)
elif solution == 2:
    import operator
    if __name__ == '__main__':
        markSheet = []
        nameSheet = []
        for _ in range(int(input())):
            name = input()
            score = float(input())
            markSheet.append([name,score])
        markSheet.sort(key = operator.itemgetter(1))
        max_score = markSheet[0][1]
        sec_score = -1;
        for i in range(len(markSheet)):
            if markSheet[i][1] != max_score and sec_score == -1:
                sec_score = markSheet[i][1]
            if sec_score != -1 and markSheet[i][1] == sec_score:
                nameSheet.append(markSheet[i][0])
        
        nameSheet.sort()
        for i in range(len(nameSheet)):
            print(nameSheet[i])