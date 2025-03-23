# Isaiah Lugo
# CSM IV - Algorithms
# Recursive Solutions

def factorial(num):
    if num == 0 or num == 1:
        return 1 # Base case: factorial(0) or factorial(1) is 1
    return num * factorial(num - 1)

def sum_list(arr):
    if not arr:
        return 0 # Base case: empty array returns 0
    return arr[0] + sum_list(arr[1:]) # Sum of first element and then recurse on list

def fibonacci(num):
    if num == 0:
        return 0 # Base case: fibonacci(0) = 0
    elif num == 1:
        return 1 # Base case: fibonacci(1) = 1
    return fibonacci(num - 1) + fibonacci(num - 2) # Recursive sum of previous two numbers

def fibonacci_sum(n):
    return sum(fibonacci(i) for i in range(n + 1)) # sum sequence up to n

def reverse_string(s):
    if len(s) == 0:
        return s # Empty strings remain empty
    return s[-1] + reverse_string(s[:-1]) # Take last character and recurse through

# Example inputs and expected outputs
print(factorial(5))  # Output: 120
print(sum_list([1, 2, 3, 4, 5, 6]))  # Output: 21
print(fibonacci_sum(6))  # Output: 12
print(reverse_string("Hello"))  # Output: olleH
