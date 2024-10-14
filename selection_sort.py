from unsorted_array import unsort

'''
Сортировка выбором
Рработает путем поиска минимального элемента в неотсортированной части массива и его обмена 
с первым элементом этой части. Затем процесс повторяется для оставшейся части массива.
'''

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print(selection_sort(unsort))
