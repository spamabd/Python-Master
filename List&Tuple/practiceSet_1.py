# Write a program to ask the user to enter name of thier 4 favorite movies & store them in a list 

# 1st Method
movies= []
mov1= input("enter your moveie 1st names")
mov2= input("enter your moveie 2nd names")
mov3= input("enter your moveie 3rd names")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#2nd Method
movies= []
movies.append(input("enter your moveie 1st names"))
movies.append(input("enter your moveie 2nd names"))
movies.append(input("enter your moveie 3rd names"))

print(movies)



# 3rd Loop Method
movies = []


for i in range(4):
    name = input(f"Enter the name of your favorite movie {i+1}: ")
    movies.append(name)


print("Your favorite movies are:", movies)