class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def InOrder(T):
    if T is not None:
        InOrder(T.left)
        print(T.item, end = ' ')
        InOrder(T.right)

def InOrderD(T, space):
    if T is not None:
        InOrderD(T.left,space +'  ')
        print(space, T.item)
        InOrderD(T.right, space + '  ')

def Smallest(T):
    if T.left is not None:
        return Smallest(T.left)
    return T

def Largest(T):
    if T.right is not None:
        return Largest(T.right)
    return T

def Find(T,k):
    if T is None or T.item == k:
        return T
    elif T.item < k:
        return Find(T.right, k)
    return Find(T.left, k)


# def Smallest(T):
#     t = T
#
#     while t.left is not None:
#         t = t.left
#     return t

T = None
T1 = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100]
for a in A:
    T = Insert(T,a)

# InOrder(T)
InOrderD(T,'')

small = Smallest(T)
large = Largest(T)
print('Smallest value in tree: %d ' % Smallest(T).item)
print('Largest value in tree: %d ' % Largest(T).item)
InOrderD(T,'')

# Find 100
found = Find(T, 100)
print('Found %d' % found.item)

found = Find(T1, 100)
print('Found %d' % found