languages = ['Python', 'Java', 'JS', 'PHP', 'Rust', 'C', 'C#']
for lang in languages:
    print(lang)
    
# for i in range(1000):
#     print(i)

# grades = {"John": 80, "Jane": 90, "Mary": 85}

# for student, grade in grades.items():
#     print(f"{student}: {grade}")
    
# names = ['John', 'Jane', 'Mary']
# ages = [20, 21, 22]

# for name, age in zip(names, ages):
#     print(f"{name}: {age}")
# my_range = range(int(input("Enter a range: ")))
# numbers = list(my_range)

# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
        
# print(f"The Even Numbers for {my_range} is {even_numbers}")

# odd_numbers = []

# for number in numbers:
#     if number % 2 != 0:
#         odd_numbers.append(number)
        
# print(f"Odd Numbers: {odd_numbers}")


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for my_number in my_numbers:
    
    total += my_number
    
print(f"Sum: {total}")