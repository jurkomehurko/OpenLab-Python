def bubble_sort(array):
    array_length = len(array)

    for i in range(array_length):
        for j in range(0, array_length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print(bubble_sort([4, 2, 5, 8, 1]))
print(bubble_sort([0.5, 4.125, 0.121, 1, 50]))
