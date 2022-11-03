import textwrap

def wrap(string, max_width):
    new_str=''
    for i in range(len(string)):
        if not (i+1)%max_width:
            new_str+=string[i]+'\n'
        else: new_str+=string[i]
    return new_str
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)