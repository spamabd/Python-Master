# factorial in function 

def fact_rec(n):
    if(n == 0 or n == 1):
        return 1
    return fact_rec(n-1) * n

print(fact_rec(4))
        