def merge_sort(list):
    """Sorts a list in ascending order and merge them. 
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and keep doing that to form sublists
    Conquer: Recursively sort the sublists
    Combine: Merge the sublists into one list of sorted elements
    
    Takes overall O(n log n) time
    """
    
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right= merge_sort(right_half)
    
    return merge(left, right)

def split(list):
    """
    Divide the unsorted list  at midpoint into sublists
    Returns two sublists= left and right
    
    Takes overall O(k log n) time, but several times
    The k comes from the split operation
    """
    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]
    
    return left, right

def merge(left, right):
    """Merges two lists into one sorted list
    
    Runs in overall O(n) time
    """
    
    l = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    
    while i < len(left):
        l.append(left[i])
        i+=1
        
    while j < len(right):
        l.append(right[j])
        j+=1
    
    return l   
        
alist = [5, 12, 7, 14, 10, 18, 3, 11]
    
result= merge_sort(alist)

print(result)
