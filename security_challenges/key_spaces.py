arr = raw_input()
n = raw_input()
print("".join([str((int(c)+int(n))%10) for c in arr]))
