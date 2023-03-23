from linked_list import LinkedList

def merge_sort(linked_list):
    """"This function sorts a linked list in ascending order
    and merges them into a single linked list
    This happens by recursively breaking the linked list
    into sublists containing a single node
    Then rep[eatedly merges the sublists into a single linked list
    until one remains
    then returns a sorted linked list
    """
    
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head == None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right= merge_sort(right_half)
    
    return merge(left, right)

def split(linked_list):
    """Divide the unsorted list at midpoint into sub linkedlists
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size// 2
        
        #mid-1 because size just like len will return n
        #we therefore need to do (n-1) 
        mid_node = linked_list.node_at_index(mid-1) 
        
        left_half = linked_list
        right_half = LinkedList()
        right_half.head =mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half
    
def merge(left, right):
    """This function merges two linkedlists,    
    sorting them by data in nodes
    Returns a new sorted merged list"""
    
    #Create a new linked list that contains nodes
    #from merging left and right
    
    merged = LinkedList()
    
    #Add a fake head which is discarded later
    merged.add(0)
    
    #Set current to the head of the linkedlist
    current = merged.head
    
    #Obtain head nodes for left and right
    left_head = left.head
    right_head = right.head
    
    #Iterate over left and right until we reach
    #tail node of either
    while left_head or right_head:
        #If the head node of left is None, then we are 
        #past the tail, then add the node from right
        #to the merged linkedlist
        if left_head is None:
            current.next_node = right_head
            #Call next on right to set the loop condition to False
            right_head = right_head.next_node
        #If the head node of right is None, we are
        #past the tail,then add the tail node from left to
        #the merged linked list
        elif right_head is None:
            current.next_node = left_head
            #Call next on left to set the loop condition to False
            left_head = left_head.next_node
        
        else:
            #Not at either tail node
            #Obtain node data to perform comparison operation
            left_data = left_head.data
            right_data = right_head.data
            #If data on left is less than data on right
            #then set current to left node
            if left_data < right_data:
                current.next_node = left_head
                #Move left head to next node
                left_head = left_head.next_node
            #If data on left is greater than data on right
            #set current to right node
            else:
                current.next_node = right_head
                #Move right head to next node
                right_head = right_head.next_node
        #Move current to next node
        current = current.next_node
    
    #Discard fake head, and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    
    return merged

l = LinkedList()
l.add(16)
l.add(67)
l.add(42)
l.add(1)
l.add(7)
l.add(97)
l.add(39)

print(l)

result= merge_sort(l)

print(result)