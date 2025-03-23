# Isaiah Lugo
# CSM IV - Algorithms
# Min and Max/Divide and Conquer

def merge_sort(list):
    if len(list) <= 1: # 1 or no elements, list is sorted already
        return list
    
    mid = len(list) // 2 # Find the middle index to split list
    left_half = merge_sort(list[:mid]) # Sort a left half
    right_half = merge_sort(list[mid:]) # Sort a right half
    
    return merge(left_half, right_half) # Merge sorted halves

def merge(left, right):
    sorted_list = [] # Initialized empty list to store sorted elements
    while left and right: # Merge two halves
        if left[0] < right[0]: # Append smaller number from left
            sorted_list.append(left.pop(0)) 
        else: # Append smaller numebr from right
            sorted_list.append(right.pop(0)) 
    sorted_list.extend(left or right) # add any remaining items from left or right
    return sorted_list

def find_max(list): # Sort the list and return last element(largest)
    sorted_list = merge_sort(list)
    return sorted_list[-1]

def find_min(list): # Sort the list and return first element(smallest)
    sorted_list = merge_sort(list)
    return sorted_list[0]

# List inputs and expected outputs
print(find_max([34, 7, 23, 32, 5, 62]))  # 62
print(find_min([34, 7, 23, 32, 5, 62]))  # 5

print(find_max([15, 3, 20, 1]))  # 20
print(find_min([15, 3, 20, 1]))  # 1

print(find_max([99, 72, 18, 44, 60, 11, 85, 23, 30]))  # 99
print(find_min([99, 72, 18, 44, 60, 11, 85, 23, 30]))  # 11

print(find_max([22]))  # 22
print(find_min([22]))  # 22
