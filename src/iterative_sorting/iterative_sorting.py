# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    for i in range(0, len(arr) - 1):
        cur_index = i

        smallest_index = cur_index

        for j in range(cur_index+1, len(arr)):

            if arr[j] < arr[smallest_index]:
                smallest_index = j

        new_num = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = new_num

    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    done = True
    while done:
        done = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


'''
 # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        small_num = arr.index(0)
        for j in range(cur_index, len(arr)-1):
            # if arr[j] < arr[cur_index]
            print(
                f'arr.index(j): {arr.index(j)}, arr.index(cur_index): {arr.index(cur_index)}')
            # if arr.index(j) < arr.index(cur_index):
            if arr.index(j) < small_num:
                # cur_index = j
                small_num = arr.index(j)
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        print(
            f'i: {i} arr: {arr.index(i)} cur_index: {cur_index}  small_num: {small_num}')

        # TO-DO: swap

    print(f'test arr: {arr}, arr lenght: {len(arr)}')
    return arr
'''

'''
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        print(f'current_index: {cur_index}')

        smallest_index = cur_index
        print(f'smallest_index: {smallest_index}')
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)-1):
            if arr.index(j) < arr.index(smallest_index):
                smallest_index = j
                print(f'smallest_index in j: {smallest_index}')
        print(
            f'test arr: {arr}, arr lenght: {len(arr)} small num: {arr.index(smallest_index)}')
        # TO-DO: swap

    return arr

'''
'''
for i in range(0, len(arr) - 1):
        cur_index = i
       

        smallest_index = cur_index
      
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        
        # TO-DO: swap

    return arr
'''
'''
 # TO-DO: swap
    arr[cur_index] = arr[smallest_index]
'''

'''
def bubble_sort(arr):
    done = False
    while done is False:
        for i in range(0, len(arr)-1):
            current_index = i
            # check position next to itself
            for j in range(current_index, current_index+1):
                if arr[j] < arr[j+1]:
                    # print('test')
                    new_num = arr[current_index]
                    arr[current_index] = arr[j]
                    arr[j] = new_num

        done = True
    return arr
'''
'''
def bubble_sort(arr):
    done = False
    while done is False:
        for i in range(0, len(arr)-1):
            current_index = i
            # check position next to itself
            for j in range(current_index, current_index+1):
                if arr[j] < arr[j+1]:
                    # print('test')
                    new_num = arr[current_index]
                    arr[current_index] = arr[j]
                    arr[j] = new_num
                    

        done = True
    return arr
'''

'''
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # print(f'current_index: {cur_index}')

        smallest_index = cur_index
        # print(f'smallest_index: {smallest_index}')
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # for j in range(cur_index, len(arr)-1):
        for j in range(cur_index+1, len(arr)):
            # print(f'heres the j {j}')
            if arr[j] < arr[smallest_index]:
                # if arr[j] < arr[cur_index]:
                smallest_index = j
                # print(f'smallest_index in j: {smallest_index} ')
        # print(
        #     f'test arr: {arr}, arr length: {len(arr)} small num: {arr[smallest_index]}')
        # TO-DO: swap
        # new_arr = arr.append(arr[smallest_index])
        new_num = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = new_num

        # print(f'New Num {new_num}')
    return arr

'''
