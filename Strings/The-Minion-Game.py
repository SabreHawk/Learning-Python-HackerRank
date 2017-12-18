def minion_game(string):
    # your code goes here
    s_score = 0
    v_score = 0
    count = 0;
    string = string.lower()
    for char in string:
        if char not in 'aeiou':
            s_score += len(string) - count
        else:
            v_score += len(string) - count
        count += 1

    if s_score > v_score:
        print("Stuart",s_score)
    elif s_score < v_score:
        print("Kevin",v_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)