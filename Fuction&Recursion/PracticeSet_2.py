# Write a function to print the element  of a list in a single line (list is the parameter).

cities = ["karachi", "lahore", "islamabad", "quetta", ]

def print_element(list):
    for item in list:
        print(item , end=" ")
        
              
print_element(cities)