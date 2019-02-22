#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:54:00 2019
@author: Esteban Andres Bustos
CS2302 Olac Fuentes MW 1:30 - 2:50 pm
TA: Anindita Nath , Maliheh Zargaran
Last Modified: Fri Feb 22, 2019
"""

############# Node Functions #############################
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
############# Node Functions #############################
############# List Functions #############################
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):
    return L.head is None

def getLength(L):
    if L.head is None:
        return 0
    else:
        tmp = L.head
        count = 0
        while tmp is not None:
            count += 1
            tmp = tmp.next
        
        return count

def Search(L,x):
    cur = L.head
    found = False
    while not found:
        if cur.item == x:
            #print('Found %d' % x)
            found = True
        else:
            cur = cur.next
    return cur
            
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Prepend(L,x):
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        tmp = Node(x)
        tmp.next = L.head
        L.head = tmp
        
def InsertAfter(L, cur, x):
    if L.head is None:
        L.head = Node(x)
        L.tail = L.head
    elif cur == L.tail:
        tmp = Node(x)
        L.tail.next = tmp
        L.tail = tmp
    else:
        current = Search(L,cur)
        tmp = Node(x)
        tmp.next = current.next
        current.next = tmp
        
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head is None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next is not None and temp.next.item != x:
             temp = temp.next
         if temp.next is not None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()     
    
def isSorted(L):
    if L.head is None:
        return True
    tmp = L.head
    
    while tmp.next is not None:
        if tmp.item > tmp.next.item:
            return False
        tmp = tmp.next
    
    return True
                
def ElementAt(L,i):
    cur = L.head
    count = 0
    
    while count != i:
        cur = cur.next
        count += 1
    return cur

def CopyList(L):
    cur = L.head
    newList = List()
    
    while cur is not None:
        Append(newList,cur.item)
        cur = cur.next
        
    return newList

def getMedian(L):
    C = CopyList(L)
    return ElementAt(C, getLength(C) // 2)

def getMid(N):
    if N is None:
        return N
    else:
        slw_ptr = N
        fst_ptr = N.next

        while fst_ptr is not None:
            fst_ptr = fst_ptr.next
            if fst_ptr is not None:
                slw_ptr = slw_ptr.next
                fst_ptr = fst_ptr.next
        return slw_ptr

############# List Methods #############################
############### Sorting Methods ########################
def bubbleSort(L):
    if IsEmpty(L):
        print('List is Empty!')
    elif getLength(L) == 1:
        print('List is already sorted')
    else:
        cur = L.head
        swapped = True
        
        while swapped:
            cur = L.head
            swapped = False
            
            while cur.next is not None:
                #print('\nIn Second While Loop')
                #Print(L)
                
                #print('\nComparing %d with %d\n' % (cur.item, cur.next.item))
                if cur.item > cur.next.item:
                    #print('Swapping...')
                    tmp = cur.item
                    cur.item = cur.next.item
                    cur.next.item = tmp
                    swapped = True
                    #print('Swapped')
                    #Print(L)
                #else:
                    #print('\nNot Swapping, Updating current node...\n')
                cur = cur.next
def Listify(N):
    newList = List()

    if N is None:
        print("Can't make a list with no node!")
    else:
        newList = List()
        # No next value, therefore Head & Tail are Node.item
        if N.next is None:
            newList.head = N
            newList.tail = N
        else:
            cur = N
            while cur is not None:
                Append(newList,cur.item)
                cur = cur.next
    return newList

def mergeSort(L):
    L = Listify(sortMerge(L.head))
    return L
                
def sortMerge(N):
    # print("\nCurrent List:")
    # Print(L)
    if N is None or N.next is None:
        return N
    else:
        ##Create Partitions
        mid = getMid(N)
        left_hd = N
        right_hd = mid.next
        mid.next = None

        return merge(sortMerge(left_hd), sortMerge(right_hd))

def merge(left,right):

    ## Base Case
    if left == None:
        return right
    if right == None:
        return left
    
    if left.item <= right.item:
        tmp = left
        cur = tmp
        cur.next = merge(left.next, right)
    else:
        tmp = right
        cur = tmp
        cur.next = merge(left, right.next)
    return tmp
############### Sorting Methods ########################
################  Main  ################################

l = [20,10,45,1,12]
L = List()
for x in l:
    Append(L,x)
    
l2 = [20,10,45,1,12]
L2 = List()
for x in l2:
    Append(L2,x)
    
l3 = [20,10,45,1,12]
L3 = List()
for x in l3:
    Append(L3,x)

print('Get Median of Lists:  \n')

print('List 1:')
Print(L)

print('Method: Bubble Sort')
bubbleSort(L)
Print(L)
med = getMedian(L)
print('Medium of List: %d\n' % med.item)

print('List 2:')
Print(L2)

print('Method: MergeSort')
L2 = mergeSort(L2)
med2 = getMedian(L2)
Print(L2)
print('Medium of List: %d' % med2.item)

#print('\nMethod: QuickSort')
#med3 = Median_QuickSort(L3)
#print('Medium of List: %d' % med3.item)
