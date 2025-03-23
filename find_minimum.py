# Isaiah Lugo
# CSM IV - Algorithms
# Assignment 2 - Algorithm Efficiency


def find_minimum_n2(arr):
    count = 0
    min_number = arr[0]
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            count += 1
            if arr[j] < min_number:
                min_number = arr[j]
    
    print("COUNT:", count)
    return min_number

def find_minimum(arr):
    count = 0
    min_number = arr[0]
    
    for num in arr:
        count += 1
        if num < min_number:
            min_number = num
    
    print("COUNT:", count)
    return min_number

# test cases
list_1 = [19, 4, 33, 11, 27]
list_2 = [42, 17, 93, 8, 67, 21, 55, 31, 74, 3]

print(find_minimum_n2(list_1))  # expected -- COUNT: 25, Result: 4
print(find_minimum(list_1))     # expected -- COUNT: 5, Result: 4

print(find_minimum_n2(list_2))  # expected -- COUNT: 100, Result: 3
print(find_minimum(list_2))     # expected -- COUNT: 10, Result: 3
