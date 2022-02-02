def bubble_sort(arr):
    for elem in range(len(arr)):
        for index in range(len(arr) - 1 - elem):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]

    return arr


print(bubble_sort([45, 36, 78, 12, 45, 67]))
