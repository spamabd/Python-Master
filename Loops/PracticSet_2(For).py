# Print the element of the following list using loop

element = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in element :
    print (num)

# Search fo a number x in this tuple using loop

element = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
 
x = 16
for val in element :
   if(val == x) :
    print("Found" , val)
    break

# Print number from 1 to 100

for val in range(1, 101):
    print(val)

# Print number from 100 to 1

for val in range( 100, 0, -1):
    print(val)

# print the multiplication table of a number n 

n = int(input("enter the number to multiplication table"))

for mul in range(1, 11):
    print(n * mul)

# write a program to find the factorial of first n number 


n = 4
Factorial = 1
i = 1
while i <= n:
   Factorial *= i
   i +=1

print(Factorial)