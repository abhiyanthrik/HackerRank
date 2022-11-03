if __name__ == '__main__':
    s = input()
    for a in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(a(c) for c in s))