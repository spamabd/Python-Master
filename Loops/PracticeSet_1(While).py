# Print number from 1 to 100
 
count = 1
while count <= 100 :
  print(count) 
  count +=1


# Print number from 100 to 1
  
count = 100
while count >= 1 :
  print(count) 
  count -=1

# print the multiplication table of n number 

n = int(input("Enter the number to give the multiplication table"))

i = 1
while i <= 10 :
    print(n*i)
    i +=1


# Print the element of the following list using loop

element = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 
i = 0
while i <len(element) :
    print(element[i]) 
    i +=1 
 
# Search fo a number x in this tuple using loop

element = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
 
x = 49
i = 0
while i <len(element) :
    if(element[i] == x) :
      print("Found" , i) 
    i +=1

# Write a program to find the sum of first n number 

n = 5
sum = 0
i = 1
while i <= n:
   sum += i
   i +=1

print(sum)