# while condition:
#     # Block of code to be executed

# count = 1
# while count <= 4:
#     print('Count:', count)
#     count += 1
    
# while True:
#     print("This runs forever")



count = 0
while count <= 15:
    
    count += 1
    if count == 10:
        continue
    # print('Count:', count)
  
# count = 1
# while count <= 5:
#     print('Count:', count)
#     count += 1
#     if count == 4:
#         break
# else:
#     print("Loop completed")
  

i = 1
while i <= 5:
    j = 1
    while j <= 3:
        # print(f"i = {i}, j = {j}")
        j += 1
    i += 1


# while True:
#     age = input('Enter your age: ')
    
#     try:
#         age = float(age)
#         if age.is_integer():
#             age = int(age)
#         print(f"Your age is {age}")
#         break
#     except:
#         print('Invalid input. Enter a valid number.')


# num = 2 
# total = 0
# while num <= 20:
#     total += num
#     num += 2
# print(total)


number = int(input("Enter a number to find its factorial: "))
factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1
    
print(f"The factorial of {number} is {factorial}")

    