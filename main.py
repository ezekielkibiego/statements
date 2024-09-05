# number = int(input("enter a number: "))
# if number > 0: 
#     print("Number is positive")
    
# elif number < 0:
#     print("Number is negative")
    
    
# else:
#     print("Number is zero")
    
    
# my_list = [1, 2, 3, 4, 5, 6]
# if not my_list:
#     print("The list is empty")
    
# elif len(my_list) == 1:
#     print("The list has one item")
    
# elif len(my_list) < 5:
#     print("The list has less than 5 items")
    
    
# else:
#     print("The list has many items")
    


my_list = [2, 3, 4, 5, 6, 'Jon Doe', True, False]
   
if not isinstance(my_list, list):
    print("The variable is not a list.")
elif not my_list:
    print("The list is empty.")
else:
    has_strings = False
    has_integers = False
    has_floats = False
    has_booleans = False
    has_others = False
    
    for item in my_list:
        if isinstance(item, str):
            has_strings = True
        elif isinstance(item, bool):
            has_booleans = True
        elif isinstance(item, int):
            has_integers = True
        elif isinstance(item, float):
            has_floats = True
        
        else:
            has_others = True
    
    if has_strings:
        print("The list contains strings.")
    if has_integers:
        print("The list contains integers.")
    if has_floats:
        print("The list contains floats.")
    if has_booleans:
        print("The list contains booleans.")
    if has_others:
        print("The list contains other types of elements.")