if __name__ == '__main__':
    gl_list = []
    for row_num in range(int(input())):
        input_line = input().split(' ')
        cmd = input_line[0]
        if cmd == "insert":
            para1 = int(input_line[1])
            para2 = int(input_line[2])
            gl_list.insert(para1,para2)
        elif cmd == "remove":
            para1 = int(input_line[1])
            gl_list.remove(para1)
        elif cmd == "append":
            para1 = int(input_line[1])
            gl_list.append(para1)
        elif cmd == "sort":
            gl_list.sort()
        elif cmd == "reverse":
            gl_list.reverse()
        elif cmd == "pop":
            gl_list.pop()
        elif cmd == "print":
            print(gl_list)


