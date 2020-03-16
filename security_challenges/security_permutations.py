
n = int(raw_input().strip())
arr = list(map(int,raw_input().split()))
for i in range(n):
    print(arr[arr[i]-1])
