# Write a recursive function to print all element in a list.

cities = ["karachi", "lahore", "islamabad", "quetta", ]

def elem_city(list, index=0):
    if(index == len(list)):
        return 
    print(list[index])
    elem_city(list, index+1)

elem_city(cities)    