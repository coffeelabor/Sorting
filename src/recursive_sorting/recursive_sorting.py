# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)

    print(f'elements: {elements}')
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    arrL = merge_sort(left)
    arrR = merge_sort(right)

    return merge(arrL, arrR)


# def merge_sort(arr):
#     if len(arr) > 1:
#         left = merge_sort(arr[:len(arr) // 2])
#         right = merge_sort(arr[len(arr) // 2:])

#         arr = merge(left, right)

#     return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) //2
    left = arr[:middle]
    right = arr[middle:]
    
    arrL = merge_sort(left)
    arrR = merge_sort(right)
    
    return merge(arrL, arrR)
'''

'''
import random

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)
    
    print('test')
    print(f'elements: {elements}')
    return merged_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) //2
    left = arr[:middle]
    right = arr[middle:]
    
    arrL = merge_sort(left)
    arrR = merge_sort(right)
    
    return merge(arrL, arrR)


# foo = random.sample(range(12), 5)
foo = [2, 4, 5, 1, 3, 9, 6]
# bar = random.sample(range(12), 5)
# merge(foo, bar)
merge_sort(foo)
'''

'''
elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    merged_arr.append(arrA, arrB)
    print('test')
    print(f'elements: {elements}')
    return merged_arr

'''
