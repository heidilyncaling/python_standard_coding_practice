numbers = [
    float(input(f"Enter number {i + 1}: "))
    for i in range(10)
]

duplicates = [
    num for num in numbers 
    if numbers.count(num) > 1
]

print(duplicates)