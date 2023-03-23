#Important tip: For binary search the list to be iterbated over has to be SORTED, as it divides the list into half and subsequent halves until we reach the end of the list

def binary_search(list, target):
    """_Returns the index of target in list, else rerurns none
    """
    first = 0
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return None

list = [1,2,3,4,5,6,7,8,9,10]

target = 5
result = binary_search(list, target)
print(result)