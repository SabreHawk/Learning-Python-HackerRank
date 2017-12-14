def split_and_join(line):
    # write your code here
    temp_line = line.split(" ")
    temp_line = "-".join(temp_line)
    return temp_line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)