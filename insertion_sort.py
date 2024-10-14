from unsorted_array import unsort

'''
Вставочная сортировка.
Работает путем сравнивания текущего элемента с предыдущим и, если они стоят в неправильном порядке, 
меняет их местами. Процесс повторяется до тех пор, пока не будет отсортирован массив.   
'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort(unsort))