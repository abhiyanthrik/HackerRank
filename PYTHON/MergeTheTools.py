def merge_the_tools(string, k):
    # your code goes here
    lst = []
    for i in range(0,len(string),k):
        substring = string[i:i+k]
        for i in substring:
            if not i in lst:
                lst.append(i)
        print(''.join(lst))
        lst.clear()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)