def selection_sort_trace():
    arr = [17, 103, 16, 35, 20, 22]
    n = len(arr)

    print("2. Selection Sort Algorithm")
    print("_" * 75)
    print("Concept: Find the minimum element in unsorted part and put it at the beginning.")

    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        current_val = arr[i]
        min_val = arr[min_idx]
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(f"Iter {i + 1} (Index {i}):")
        print(f"Min is {min_val}. Swap {current_val} & {min_val}")
        print("->")
        print(f"{arr}")

    print(f"Sorted Array: {arr}")

selection_sort_trace()
