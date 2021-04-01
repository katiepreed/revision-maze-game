# divide-and-conquer sorting algorithm
# works by splitting the list into halves until separate elements remain.
# then it sorts each half and merges the lists together.
# time complexity is O(nlogn)
# because the list is being split log(n) times and the merging process is linear.

# this is the recursive approach for implementing merge sort.
def merge_sort(my_list):
    if len(my_list) > 1:
        # the list is divided into left and right in each recursive call until two adjacent elements are obtained.
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursive call on each half of the list
        merge_sort(left)
        merge_sort(right)

        # the i and j iterators traverse the two halves in each call.
        i = 0
        j = 0

        # the k iterator traverses the whole list and makes changes along the way
        k = 0

        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1]:
                # my_list[k] holds the greater value
                # if the value at i is greater than the value at j
                #  then left[i] is assigned to the myList[k] slot
                my_list[k] = left[i]
                # i is incremented
                i += 1
            else:
                # if value at j is greater than the value at i
                # then my_list[k] = right[j]
                my_list[k] = right[j]
                # j is incremented
                j += 1
            # k is incremented
            # this means we move to the next item
            # this way the values assigned through k are all sorted
            k += 1

        # at the end of the previous loop one of the halves may have not been traversed completely .
        # it's values are assigned to the remaining slots in the list.
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1

    return my_list