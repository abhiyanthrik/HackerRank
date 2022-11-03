def count_substring(string, sub_string):
    strlen = len(string) - len(sub_string) + 1
    end = len(sub_string)
    s = 0
    for i in range(strlen):
        if string[i:end + i] == sub_string:
            s += 1
    return s


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)