#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >=0 or idx < len(my_list):
        new_list= my_list[:]
        new_list[idx]= element
        return new_list
    
    
    
original_list = [1, 2, 3, 4, 5]
idx = 2
new_element = 10
updated_list = new_in_list(original_list, idx, new_element)
print("Original list:", original_list)
print("Updated list:", updated_list)