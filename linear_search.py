#Important tip : For linear search the list DOES NOT have to be SORTED, as it itertaes over each elemnet until the end of the list

def linear_search(list, target):
    """
    Returns the position of the index of the target if found in the list, else returns none
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
               
list = [1,2,3,4,5,6,7,8,9,10]

target = 4
result = linear_search(list, target)
print(result)
    
    
        