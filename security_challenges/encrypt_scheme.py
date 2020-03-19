
def get_fact(n):
    if n==1:
        return 1
    return n * get_fact(n-1)

n = int(raw_input())
print(get_fact(n))
