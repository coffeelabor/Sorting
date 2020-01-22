# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    
    for i in range(0, len(arr)-1):
        current_index = i
        smallest_index = current_index

        for j in range(current_index+1, len(arr)):
            if arr[j]< arr[smallest_index]:
                smallest_index = j

        new_num = arr[current_index]
        arr[current_index] = arr[smallest_index]
        arr[smallest_index] = new_num

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    complete = True
    while complete:
        complete = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                complete =True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


'''
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # print('arr', arr)
    for i in range(0, len(arr) - 1):
        cur_index = i
        # print('cur_index', cur_index)
        smallest_index = cur_index
        # print('smallest_index', smallest_index)
        # print('cur_index', cur_index)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             
        for j in range(cur_index+1, len(arr)):
            # print('j', j)
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                # print('smallest_index', smallest_index)

        # TO-DO: swap
        new_num = arr[cur_index]
        # print('new_num 1', new_num)
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = new_num
        # print('new_num 2', new_num)
        

    # print('arr', arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    complete = True
    while complete:
        complete = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                complete =True

    return arr

'''
