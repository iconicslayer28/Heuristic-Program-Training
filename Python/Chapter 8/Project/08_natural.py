def fact_rec(n):
    if n==1 or n==0:
        return 1
    return n + fact_rec(n-1)
        
s = fact_rec(10)
print(s)