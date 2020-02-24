# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
fx = []
f = raw_input()  
fx = list(map(int,f.split(' '))) 

if len(fx) == n:
    print ("YES")
else: print("NO") 
