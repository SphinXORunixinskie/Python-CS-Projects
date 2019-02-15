import random, time

def bubble_sort(a_list):
    for pass_num in range(len(a_list)-1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
        
def merge_sort(a_list):
    print("Splitting", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
                
            else: 
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1
            
            while i < len(left_half):
                a_list[k] = left_half[i]
                i = i + 1
                k = K + 1
                
            while j < len(right_half):
                a_list[k] = right_half[j]
                j = j + 1
                k = k + 1 
                
            print("Merging", a_list)     
            
def selection(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
                
        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp
        

def randomlist(n):
    listx = {}
    for i in range(n):
        listx[i] = random.randint(0, 100)
    return listx
        
    
'''
Implementation of the Binary Tree ADT defined in Section 6.4.2 
of the textbook (pdf version)
'''

class BinaryTree:
    '''
    Constructor initializes key to value provided (root).
    Left and right child references are None.  
    '''
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None
        
    '''
    Create new binary tree and insert it as left child of 
    current node.
    '''
    def insert_left(self, new_node):
        # if left child is None, create new node and modify 
        # the left reference
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        # otherise, create new node and modify the left 
        # reference of the current node so that it 
        # references new node
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
        
    '''
    Create new binary tree and insert it as right child of 
    current node.
    '''        
    def insert_right(self, new_node):
        # if there's no right child, create new node
        # and make it right child of current node
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        # otherise, create new node and modify the right 
        # reference of the current node so that it 
        # references new node
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
            
    '''
    Return right subtree
    '''    
    def get_right_child(self):
        return self.right_child
                
    '''
    Return left subtree
    '''
    def get_left_child(self):
        return self.left_child
         
    '''
    Modify the value of the current node
    '''       
    def set_root_val(self, obj):
        self.key = obj
     
    '''
    Get the value of the current node
    '''           
    def get_root_val(self):
        return self.key
    
   
# External implementations of tree traversal methods (i.e. Not
# part of the class definition).  Must be called with the tree
# reference as the argument.  
    
'''
Preorder tree traversal: Visit the root node first, then 
recursively do a preorder traversal of the left subtree, 
and finally a recursive preorder traversal of the right 
subtree.
'''
def preorder(tree):
    if tree:
        print(tree.get_root_val(), end = " ")
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

'''
Postorder tree traversal: Recursive postorder traversal of 
the left subtree, followed by a recursive postorder traversal 
of the right subtree, and finally visit the root.
'''
def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val(), end = " ")        

'''
Inorder tree traversal: Recursively do an inorder traversal 
of the left subtree, visit the root, and finally do a 
recursive inorder traversal of the right subtree.
'''
def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val(), end = " ")
        inorder(tree.get_right_child())


def main():      
    
    output_list = {} 
    for x in range(1,9):
        output_list[x*10000] = {"selection":selection(randomlist(x*10000)), "bubble":bubble_sort(randomlist(x*10000)), "merge":merge_sort(randomlist(x*10000)), "tree":tree_sort(randomlist(x*10000))}
    print(output_list)

def time_ms():
    return int(round(time.time()*100))

def selection_sort(rlist):
    temp = time_ms()
    selection_sort(rlist)
    runtime = time_ms() - temp
    return runtime
    
def bubble_flip(rlist):
    temp = time_ms()
    bubble_sort(rlist)
    runtime = time_ms() - temp
    return runtime 

def merge_split(rlist):
    temp = time_ms()
    merge_sort(rlist)
    runtime = time_ms() - temp
    return runtime 

def tree_node(rlist):
    temp = time_ms()
    tree_sort(rlist)
    runtime = time_ms() - temp
    return runtime
        

if __name__ == "__main__":
    main()


        