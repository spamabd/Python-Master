# print n to 1 backwards using recursion method 

def call_back(n):
    if(n == 0):
         return
    print(n)
    call_back(n-1)

call_back(5)

# this function is also called recursive function