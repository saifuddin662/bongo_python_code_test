# create node class to save node instance values
class Node:  
    def __init__(self, value): 
        self.value =  value 
        self.left = None
        self.right = None

# check for path from root and store ancestor to path list
def findPath( my_root, path, node ): 

    if my_root is None: 
        return False

    path.append(my_root.value) 

    if my_root.value == node : 
        return True

    if ((my_root.left != None and findPath(my_root.left, path, node)) or
            (my_root.right!= None and findPath(my_root.right, path, node))): 
        return True 

    path.pop() 
    return False
 
 # find the ica of two given node
def ica(my_root, node1, node2): 
  
    path1 = [] 
    path2 = [] 

    if (not findPath(my_root, path1, node1) or not findPath(my_root, path2, node2)): 
        return -1 

    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 

# create a demo binary tree following sample input 
my_root = Node(1) 
my_root.left = Node(2) 
my_root.right = Node(3) 
my_root.left.left = Node(4) 
my_root.left.right = Node(5) 
my_root.right.left = Node(6) 
my_root.right.right = Node(7) 
my_root.left.left.left = Node(8)
my_root.left.left.right = Node(9)

# showing result of demo example from question
print(ica(my_root, 6, 7))
print(ica(my_root, 3, 7))