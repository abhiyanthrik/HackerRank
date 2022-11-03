'''
def minion_game(string):
    # your code goes here
    string = string.lower()
    st = 0
    ke = 0
    hash = []
    vowels = 'a e i o u'.split()
    for i in range(len(string)):
        for j in range(1,len(string)-i+1):
            sub_string = string[i : i+j]
            if not sub_string in hash:
                hash.append(sub_string)
                s_new = string
                while sub_string in s_new:
                    s_new=s_new[s_new.find(sub_string)+1:]
                    if sub_string[0] in vowels:
                        ke += 1
                    else:
                        st += 1
                        
    if st > ke: print('Stuart',st)
    elif st < ke : print('Kevin',ke)
    else: print('Draw')

#An optimized approach
def minion_game(string):
    # your code goes here
    string = string.lower()
    st = 0
    ke = 0
    vowels = 'a e i o u'.split()
    for i in range(len(string)):
        sub_string = string[i:]
        if sub_string[0] in vowels:
            ke += len(sub_string)
        else: st += len(sub_string)
                        
    if st > ke: print('Stuart',st)
    elif st < ke : print('Kevin',ke)
    else: print('Draw')
'''

#The Solution
def minion_game(string):
    # your code goes here
    string = string.lower()
    st = 0
    ke = 0
    vowels = 'a e i o u'.split()
    for i in range(len(string)):
        if string[i] in vowels:
            ke += len(string) - i
        else: st += len(string) - i
                        
    if st > ke: print('Stuart',st)
    elif st < ke : print('Kevin',ke)
    else: print('Draw')
                

if __name__ == '__main__':
    s = input()
    minion_game(s)