from unsorted_array import unsort

'''
Быстрая сортировка
Работает путем разделения массива на две части: элементы, которые меньше опорного элемента, 
и элементы, которые больше опорного. Затем процесс повторяется для полученных двух частей.
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort(unsort))
