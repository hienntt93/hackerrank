# Enter your code here. Read input from STDIN. Print output to STDOUT
def bijective(n,f):
    for i in range(0,n):
        for j in range(0,i):
            if(j+1) in f:
                continue
            else: return ("NO")
    return "YES"
n = int(raw_input())
f = list(map(int,raw_input().split())) 

print(bijective(n,f))
