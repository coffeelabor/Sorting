# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
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
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    pivot = len(arr) //2
    left = arr[:pivot]
    right = arr[pivot:]


    leftArr = merge_sort(left)
    rightArr = merge_sort(right)


    return merge(leftArr, rightArr)
    # return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

'''
# print('elements', elements)
for i in range(0, elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else: merged_arr[i] = arrB.pop(0)
    print('merged_arr', merged_arr)
print('merged_arr', merged_arr)
'''

'''
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    pivot = len(arr) //2
    left = arr[:pivot]
    right = arr[pivot:]

    print('left', left)
    print('right', right)

    leftArr = merge_sort(left)
    rightArr = merge_sort(right)
    print('leftArr', leftArr)
    print('rightArr', rightArr)

    return merge(leftArr, rightArr)
'''
