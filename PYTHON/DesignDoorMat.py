# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M = map(int,input().split())
string = ".|."
wellcome = 'WELCOME'
for i in range(N//2):
    n = string*(2*i+1)
    n = n.center(M,'-')
    print(n)
print(wellcome.center(M,'-'))
for i in range(N//2-1,-1,-1):
    n = string*(2*i+1)
    n = n.center(M,'-')
    print(n)