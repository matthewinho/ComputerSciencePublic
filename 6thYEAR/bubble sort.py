
def bubble_sort(arr):
    n = len(arr)
    swapped = True
    phase = 0 
    
    while swapped:
        swapped = False
        for i in range(1, n):
            phase = phase +1
            print(arr,"PHASE", phase)
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
                
        n -= 1

    return arr
unsorted_list =  [int(item) for item in input("Enter the list items with space between : ").split()]


#unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Sorted List:", sorted_list, "[FINAL PHASE COMPLETE]")
