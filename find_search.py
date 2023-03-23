
def find_missing(list):
    """Returns the missing number in a sorted list"""
    for i in range(len(list)):
        if list[i] != i +list[0]:
            return i + list[0]
    return None
    
list = [1,2,4,5]

print(find_missing(list))