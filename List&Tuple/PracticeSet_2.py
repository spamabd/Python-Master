# Write a program to check if a list contain a palindrome of element 

list1= [1, 2, 1]

copy_list=list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("this is palindrome")
else:
    print("this is not a palindrome")     