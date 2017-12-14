solution = 1 
if solution == 1:
    S = input()
    print (any([char.isalnum() for char in S]))
    print (any([char.isalpha() for char in S]))
    print (any([char.isdigit() for char in S]))
    print (any([char.islower() for char in S]))
    print (any([char.isupper() for char in S]))
else:
    if __name__ == '__main__':
        str = input()
        detecArr = [0 for i in range(5)]
        for s in str:
            if s.isalnum():
                detecArr[0] = 1
            if s.isalpha():
                detecArr[1] = 1
            if s.isdigit():
                detecArr[2] = 1
            if s.islower():
                detecArr[3] = 1
            if s.isupper():
                detecArr[4] = 1
        for i in range(len(detecArr)):
            if detecArr[i] == 1:
                print("True")
            else :
                print("False")
            
    