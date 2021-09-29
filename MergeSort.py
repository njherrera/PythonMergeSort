def mergeSort(list):
    # if list is length 1, return list
    if len(list) <= 1:
        return list
    # make one empty list for left side, one for right side
    leftSide = []
    rightSide = []
    # add first half of og list to left, right half to right side
    for index, element in enumerate(list):
        if index < len(list) // 2:
            leftSide.append(element)
        else:
            rightSide.append(element)
    # call mergeSort on left
    # call mergeSort on right
    leftSide = mergeSort(leftSide)
    rightSide = mergeSort(rightSide)

    # return merge(left, right)
    return merge(leftSide, rightSide)

def merge(left, right):
    # make new empty list (result)
    result = []


    # while left and right are not empty:
        # if the first item of left is <= first item of right, append first item of left to result
        # else append first item of right to result
    if not left and not right:
        result.append(left[0])
        left = left[1:]

    # now either left or right is not empty
    # while left is not empty:
        # append first item of left to result

    # while right is not empty:
        # append first item of right to result

    # return result