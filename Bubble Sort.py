def bubble_sort_trace():
    arr = [17, 103, 16, 35, 20, 22]
    n = len(arr)
    
    print("1. Bubble Sort Algorithm")
    print("_" * 75)
    print("Concept: Compare adjacent elements and swap them if in wrong order.\n")

    for i in range(n):
        swapped = False
        if i < 3: 
            print(f"Pass {i + 1}:")

        for j in range(0, n - i - 1):
            val1 = arr[j]
            val2 = arr[j+1]
            action = "No swap"
            
            if val1 > val2:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                action = "Swap   "
            
            if i < 2: 
                print(f"Compare ({val1}, {val2}): {action} -> {arr}")


        if i == 0:
            print("Result: Largest element (103) reaches the end.\n")
        elif i == 1:
            print("\n", end="") 
        elif i == 2 and not swapped:
            print("No swaps needed. Array is sorted.")
            break
            
    print(f"Sorted Array: {arr}")

bubble_sort_trace()
