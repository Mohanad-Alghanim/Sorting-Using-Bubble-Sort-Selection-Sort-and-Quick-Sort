step_counter = 1

def quick_sort_trace(arr):
    global step_counter
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    print(f"Step {step_counter} (Pivot {pivot}):")
    print(f"L:{left} | R:{right}")
    
    state_str = ""
    if left: state_str += f"{left} + "
    state_str += f"{pivot}"
    if right: state_str += f" + {right}"
    
    print(f"State: {state_str}")
    step_counter += 1
    
    return quick_sort_trace(left) + [pivot] + quick_sort_trace(right)

print("3. Quick Sort Algorithm")
print("_" * 75)
print("Concept: Partition array around a pivot (first element).")

my_array = [17, 103, 16, 35, 20, 22]
sorted_arr = quick_sort_trace(my_array)
print(f"Sorted Array: {sorted_arr}")
