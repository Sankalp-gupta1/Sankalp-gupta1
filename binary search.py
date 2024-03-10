def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]
        if mid_element == target:
            return mid  
        elif mid_element < target:
            low = mid + 1 
        else:
            high = mid - 1  
    return -1 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 9
result = binary_search(my_list, target_element)
if result != -1:
    print(f"Element {target_element}  mil gaya hai ghar jao aab ▼ lkin index number {result} pe mila hai.")
else:
    print(f"Element {target_element} nahi mil ra hai bhaiiiiiiiiiiiiiii check karo error.")
