def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers) 

#Example usage:
print(calculate_average([1,2,3,4,5]))
print(calculate_average([]))