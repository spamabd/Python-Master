# write a function that take input in number and print the result if is number is odd show result in string is "ODD" and same as even.

n = int(input("enter the number to find the factorial:" ))

def checker(n):
    if(n % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

checker(n)        