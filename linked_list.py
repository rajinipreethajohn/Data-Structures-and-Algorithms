class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    
    data = None
    next_node = None
    
    
    def __init__(self, data):
        self.data = data
    
        
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    Singly linked list
    """
    
    def __init__(self):
        self.head = None
    
        
    def is_empty(self):
        return self.head is None
    
    
    def size(self):
        """
        Returns the number of nodes in the, 
        takes O(n) ie (Big O of n)time
        """
        current= self.head
        count = 0
        
        while current is not None:
            count += 1
            current = current.next_node
            
        return count


    def add(self, data):
        """Adds a new node contatining data at the head of the list
        this operation takes O(1) ie constant time """
        
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    
    def search(self, key):
        """Search data for key input, returns the node if found else None
        Takes O(n) time"""

        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node        
        return None
    
    
    def insert(self, data, index):
        """Inserting a new node containing data based on the index which is a O(1) time
        But inserting requires traversing the Linked list which is O(n) time
        so totally it will ne O(n)time"""
        
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head
            
            while position > 1:
                current = current.next_node
                position -= 1
            previous = current
            next = current.next_node
            
            previous.next_node = new
            new.next_node = next
                
    def remove(self, key):
        """Removes the data that matches the given key and returns  
        None if the key is not present. 
        
        Thus takes O(n)time as we have to traverse through the list
        """
        
        current = self.head
        previous = None
            
        found = False
            
        while current and not found:
                if current.data == key and current is self.head:
                    found = True
                    self.head = current.next_node
                elif current.data == key:
                    found = True
                    previous.next_node = current.next_node
                else:
                    previous = current
                    current = current.next_node
        return current
    
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            
            while position <  index:
                current = current.next_node
                position += 1
                
            return current
            
                   
    def __repr__(self):
        """Returns a string representation of the list"""
        
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head : %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail : %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        return '-> '.join(nodes)