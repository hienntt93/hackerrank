# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(raw_input())
s = list(map(int,raw_input().split()))

for t in range(n):
    print (s.index(t+1)+1)
