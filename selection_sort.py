def Selection_sort(arr):
    for i in range(len(arr)):  # looping the array to check for all element
        min_index = i  # selecting the min element in this case (first index element).
        for j in range(i + 1, len(arr)):  # looping from one index ahead elem from the min elem to the len(arr)
            if arr[min_index] > arr[j]:  # checking if min index element is greater than the one ahead or not
                min_index = j  # if true then make min_index to be equal to j.

        arr[i], arr[min_index] = arr[min_index], arr[i]  # swaping the element

    return arr


print(Selection_sort([34, 2, 56, 28, 64]))
