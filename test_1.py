def sort_and_split(numbers):
    numbers.sort()
    even = [num for num in numbers if num % 2 == 0]
    odd = [num for num in numbers if num % 2 != 0]
    return even, odd

# Example usage:
nums = [5, 2, 8, 1, 9, 4]
even_list, odd_list = sort_and_split(nums)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
