# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
nmb = list(map(int,raw_input().split()))
for i in range(0,n):
    try: 
        if i+1 != nmb[nmb[i]-1]:
            print "NO"
            exit(0)
    except IndexError:
        print("NO")
        exit(0)
print "YES"
