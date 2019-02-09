"""
Created on Sun Feb  3 20:02:10 2019

@author: Esteban Andres Bustos
Class: CS2302 MWF 1:30 - 3:20pm
Last Modified: Feb 3 2019
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import math
import matplotlib.pyplot as plt
import os

def drawSquares(ax,n,p,w):
    if n > 0:
        i1 = [1,2,3,0,1]
        ## Base Case
        ax.plot(p[:,0], p[:,1], color='k')
        
        ## Recursive Call
        q = p*w + p[i1] * (1-w)
        drawSquares(ax,n-1,q,w)
        
def drawMultiSquares(ax,n,p):
    if n>0:
        #print('Square Layer %d\n' % n) 
        #print('plotting coordinates:\n', p)
        
        ### Base Case
        ax.plot(p[:,0],p[:,1], color='k')
        
        a = p[1] - p[0]
        rad = (math.sqrt(a[1]**2)) / 2
        mid = p[0] + rad
        
        #print('\nLength of square sides: %d\n' % a[1])
        #print('Midpoint of square: \n', mid)
        #print('\nRadius of Square: %d\n' % rad)
        
        ### Recursive Call
        if n > 1:
            for x in range(4):
                q = np.array([[p[x,0] - rad/2, p[x,1] - rad/2],
                              [p[x,0] - rad/2, p[x,1] + rad/2],
                              [p[x,0] + rad/2, p[x,1] + rad/2],
                              [p[x,0] + rad/2, p[x,1] - rad/2],
                              [p[x,0] - rad/2, p[x,1] - rad/2]])
                #print('Created square %d, now going to plot square at point %d ...' %(x+1, x))
                drawMultiSquares(ax,n-1,q)
        else:
             return #print('Done with square. Returning to previous call.\n')
                     
            
def circle(center, rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def drawCircles(ax,n,center,radius,w):
    if n>0:
        ## Base Case
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        ## Recursive Call
        drawCircles(ax,n-1,center,radius*w,w)
        
def drawShiftedCircles(ax,n,center,radius,w):
    #print('\nCircle Layer %d' % n)
    if n > 0:
        ### Base Case
        x,y = circle(center, radius)
        ax.plot(x,y,color='k')
        ### Recursive Call
        #print('Initial Center Point:', center)
        #print('Radius: %d' % radius)
        for x in range(len(center)):
            center[x-1] = center[x-1] * w
        #print('New Center Point:', center)
        drawShiftedCircles(ax,n-1,center,radius*w,w)

def createTree(ax,n,p):
    print('\nN = %d' % n)
    ## Base Case
    if n == 0:
        #c = np.array([[p[0], p[1]]])
        #print('Returning:\n',c)
        print('At leaf returning')
        print(p)
        
        return p
    if n >= 1:
        print('Current Tree:')
        print(p)
        
        x = p[0,0]
        left = np.array([[x - x/2, x]])
        right = np.array([[x + x/2,x]])
        
        print('\nLeft Child: ')
        print(left)
        print('\nRight Child: ')
        print(right)
        
        ##Left Child
        print('\nAppending and going to left child')
        p = np.append(p, createTree(ax,n-1,left), axis=0)
        print('\nReturned from left child.\nNew Tree:')
        print(p)
    
        ##Parent
        parent = np.array([[p[0,0], p[0,1]]])
        print('\nAppending parent: ')
        print(parent)
        p = np.append(p, parent, axis=0)
        print('\nNew Tree:')
        print(p)

        ##Right Child
        print('\nAppending and going to right child')
        p = np.append(p, createTree(ax,n-1,right), axis=0)
        print('\nReturned from right child.\nNew Tree:')
        print(p)
        
        ##Parent
        parent = np.array([[p[0,0], p[0,1]]])
        print('\nAppending parent: ')
        print(parent)
        p = np.append(p, parent, axis=0)
        print('\nNew Tree:')
        print(p)
        return p
    
    
def drawTree(ax,n,p):
    if n == 0:
        print('At root')
        print(p)
        return
    else:
        p = createTree(ax,n,p)
        print('\nDone with creating tree: ')
        print(p)
        ax.plot(p[:,0],p[:,1], color='k')
############################ functions end here ###########################################

plt.close("all")
orig_size = 1000

path = "Lab1_Output_Images"

try:
    os.mkdir(path)
except OSError:
    print("Failed to create directory '%s' as it already exists" % path)
else:
    print("Created path %s successfully" % path)
    
# Different Lab Figures:

### Problem 1
## Sqaures

# a
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
ax.axis('on')
ax.set_aspect(1.0)
drawSquares(ax,10,p,.2)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_1a.png')

# b
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawSquares(ax,10,p,.1)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_1b.png')

# c
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawSquares(ax,100,p,.1)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_1c.png')

## Circles
# a
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawCircles(ax, 3, [100,0], 100,.5)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_2a.png')

# b
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawCircles(ax, 30, [100,0], 100,.87)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_2b.png')

# c
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawCircles(ax, 100, [100,0], 100,.92)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_2c.png')

## Problem 2
# a
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawMultiSquares(ax,2,p)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_3a.png')

# b
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawMultiSquares(ax,3,p)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_3b.png')

# c
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawMultiSquares(ax,4,p)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_3c.png')

## Problem 3
# a
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawShiftedCircles(ax,10,[100,0], 100,.55)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_4a.png')

# b
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawShiftedCircles(ax,55,[100,0], 100,.55)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_4b.png')

# c
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect(1.0)
drawShiftedCircles(ax,65,[100,0], 100,.90)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_4c.png')

## Problem 4
# a
p = np.array([[orig_size/2,orig_size]])
fig, ax = plt.subplots()
ax.axis('on')
ax.set_aspect(1.0)
drawTree(ax,2,p)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_5a.png')
