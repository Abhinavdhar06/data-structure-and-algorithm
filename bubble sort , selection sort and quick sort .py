#bubble sort

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage of Bubble Sort
arr_bubble = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr_bubble)
print("Bubble Sorted Array:", arr_bubble)

#selection sort

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage of Selection Sort
arr_selection = [64, 25, 12, 22, 11]
selection_sort(arr_selection)
print("Selection Sorted Array:", arr_selection)

##quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage of Quick Sort
arr_quick = [5, 3, 8, 6, 7, 2, 1, 4]
sorted_arr_quick = quick_sort(arr_quick)
print("Quick Sorted Array:", sorted_arr_quick)
