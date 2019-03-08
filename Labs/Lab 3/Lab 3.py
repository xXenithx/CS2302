"""
Created on Sun Mar 3 2:59:57 2019

@author: Esteban Andres Bustos
Class: CS2302 MWF 1:30 - 3:20pm
Last Modified: Mar 3 2019
"""

import matplotlib.pyplot as plt
import numpy as np
import math


class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


def circle(center, rad):
    n = int(4 * rad * math.pi)
    t = np.linspace(0, 6.3, n)
    x = center[0] + rad * np.sin(t)
    y = center[1] + rad * np.cos(t)
    return x, y

def DrawNode(T, center, rad, ax):
    if T is not None:
        x, y = circle(center, rad)
        ax.plot(x, y, color='k', linewidth=2.5, zorder=1)
        ax.fill(x,y,color='white', zorder=3)
        ax.text(center[0], center[1], str(T.item), horizontalalignment='center', verticalalignment='center',
                fontsize=6.5, zorder=4)


def DrawTree(T, center, xMax, yMax, rad, w, ax):
    if T is not None:
        ctr_left = [center[0] - xMax, center[1] - yMax]
        ctr_right = [center[0] + xMax , center[1] - yMax]

        if T.left is not None and T.right is not None:
            #Left Branch
            ax.plot([center[0], ctr_left[0]] ,[center[1], ctr_left[1]] ,color='k', zorder=2)
            #Right Branch
            ax.plot([center[0], ctr_right[0]] ,[center[1], ctr_right[1]] ,color='k',zorder=2)

        if T.left is not None and T.right is None:
            ax.plot([center[0], ctr_left[0]] ,[center[1], ctr_left[1]] ,color='k',zorder=2)

        if T.right is not None and T.left is None:
            ax.plot([center[0], ctr_right[0]] ,[center[1], ctr_right[1]] ,color='k',zorder=2)

        DrawNode(T, center, rad, ax)

        # Goto Left child
        DrawTree(T.left, ctr_left, xMax/w, yMax, rad, w, ax)
        # Goto Right child
        DrawTree(T.right, ctr_right, xMax/w, yMax, rad, w, ax)


def Insert(T, newItem):
    if T == None:
        T = BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left, newItem)
    else:
        T.right = Insert(T.right, newItem)
    return T


def Delete(T, del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left, del_item)
        elif del_item > T.item:
            T.right = Delete(T.right, del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None:  # T is a leaf, just remove it
                T = None
            elif T.left is None:  # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left
            else:  # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right, m.item)
    return T


def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item, end=' ')
        InOrder(T.right)


def InOrderD(T, space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right, space + '   ')
        print(space, T.item)
        InOrderD(T.left, space + '   ')


def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T


def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)


def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)


def Find(T, k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item < k:
        return Find(T.right, k)
    return Find(T.left, k)


def FindAndPrint(T, k):
    f = Find(T, k)
    if f is not None:
        print(f.item, 'found')
    else:
        print(k, 'not found')


def FindIter(T, k):
    cur = T
    while cur is not None:
        if cur.item == k:
            return cur
        elif cur.item > k:
            cur = cur.left
        else:
            cur = cur.right
    return None

def InsertSorted(Tree, arr):
    if len(arr) != 0:
        for x in range(len(arr)):
            if Tree is None:
                Tree = BST(arr[x])
            Tree = Tree.right

# Code to test the functions above
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T, a)

T1 = None
A1 = [10,4,15,2,8,12,18,1,3,5,9,7]
for a1 in A1:
    T1 = Insert(T1,a1)

U = None
B = [1,2,3,4,5,6,7,8,9]
for b in B:
    U = Insert(U,b)

# InOrderD(T, "")

plt.close()
fig, ax = plt.subplots()
ax.axis('on')
ax.set_aspect(1.0)
DrawTree(T1, [0, 0], 55, 50, 7, 1.6, ax)
plt.show()


# plt.close()
# fig, ax = plt.subplots()
# ax.axis('on')
# ax.set_aspect(1.0)
# DrawTree(U, [0, 0], 100, 10, 1, ax)
# plt.show()

key = 7
print('Looking for k: %d' % key)
found = FindIter(U,key)
if found is not None:
    print('Found %d' % found.item)
else:
    print('Key %d was not found!' % key)

print('Creating tree with a sorted list..')
arr = [5,6,7,8,9,10]
T1 = None
InsertSorted(T1,arr)
InOrderD(T1, "")
