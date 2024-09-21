# Write a program to print grade that taken input marks of the user

Marks = int(input("Enter the marks to get the grade")) 

if Marks >=90:
    print("your grade is A")
elif Marks>=80:
    print("your grade is B")
elif Marks>=70:
    print("your grade is C")
elif Marks>=60:
    print("your grade is D")
else:
    print("Your grade is F")