def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        # Compare adjacent elements
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred, array is already sorted
        if not swapped:
            break

    return arr


# Example
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)
print("Sorted array:", bubble_sort(arr))
print("Enrollment number:92460118241")
