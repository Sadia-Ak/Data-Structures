def merge_sort(array):
    
    if len(array) > 1:

        # mid is an index where the array is divided into two halves
        mid = len(array)//2
        a1 = array[:mid]
        a2 = array[mid:]

        # recursively call mergesort function on divided arrays
        merge_sort(a1)
        merge_sort(a2)

        i = j = k = 0

        # pick the large element of array1 or array2, whichever reaches the end first and
        # put them in their correct position
        while i < len(a1) and j < len(a2):
            if a1[i] < a2[j]:
                array[k] = a1[i]
                i += 1
            else:
                array[k] = a2[j]
                j += 1
            k += 1

        # when the elements in either of the arrays are sorted, pickup the remaining elements
        # from the other array and sort them
        while i < len(a1):
            array[k] = a1[i]
            i += 1
            k += 1

        while j < len(a2):
            array[k] = a2[j]
            j += 1
            k += 1

def De_dulplication(array):

    # sort the array using mergesort
    merge_sort(array)

    # index of the array
    i = 0

    # iterate through the elements of the array
    while i < len(array)-1:

        # if the element in the current position is the same as the next element
        # remove the next element
        # else
        # change position to the next element
        if array[i] == array[i+1]:
            array.remove(array[i+1])
        else:
            i += 1

    # return the modified array to the main method
    return array

if __name__ == '__main__':
    # an array given in the example
    array1 = [50, 11, 33, 21, 40, 50, 40, 40, 21]
    De_dulplication(array1)
    print(array1)

    # a null array
    array2 = []
    De_dulplication(array2)
    print(array2)

    #array with single element
    array3 = [10]
    De_dulplication(array3)
    print(array3)

    #array with no-duplicates
    array3 = [10, 30, 20, 15, 50]
    De_dulplication(array3)
    print(array3)

    #array that is already sorted
    array5 = [10, 10, 20, 30, 30, 45, 50]
    De_dulplication(array5)
    print(array5)


