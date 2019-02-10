"""
Created on Sun Feb  3 20:02:10 2019

@author: Esteban Andres Bustos
Class: CS2302 MWF 1:30 - 3:20pm
Last Modified: Feb 10 2019
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
        
        "Base Case"
        ax.plot(p[:,0], p[:,1], color='k')
        
        "Recursive Call"
        q = p*w + p[i1] * (1-w)
        drawSquares(ax,n-1,q,w)
        
def drawMultiSquares(ax,n,p):
    if n>0:
        #print('Square Layer %d\n' % n) 
        #print('plotting coordinates:\n', p)
        
        "Base Case"
        
        """
        Base Case is plotting all the points in the first square.
        """
        
        ax.plot(p[:,0],p[:,1], color='k')
        
        """
        Gets the side length of the current and finds the radius by squaring the length^2 divied by 2
        """
        a = p[1] - p[0]
        rad = (math.sqrt(a[1]**2)) / 2
        
        #mid = p[0] + rad
        #print('\nLength of square sides: %d\n' % a[1])
        #print('Midpoint of square: \n', mid)
        #print('\nRadius of Square: %d\n' % rad)
        
        "Recursive Call"
        
        ""
        "Recursively adding new square points to new array 4 times and passes to recursive function to plot"    
        ""
        
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
            """
            Doesn't create more squares if n < = 0
            """
            return #print('Done with square. Returning to previous call.\n')
                     
            
def circle(center, rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def drawCircles(ax,n,center,radius,w):
    if n>0:
        "Base Case"
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        
        "Recursive Call"
        drawCircles(ax,n-1,center,radius*w,w)
        
def drawShiftedCircles(ax,n,center,radius,w):
    #print('\nCircle Layer %d' % n)
    if n > 0:
        "Base Case"
        x,y = circle(center, radius)
        ax.plot(x,y,color='k')
        "Recursive Call"
        #print('Initial Center Point:', center)
        #print('Radius: %d' % radius)
        
        for x in range(len(center)):
            center[x-1] = center[x-1] * w
        #print('New Center Point:', center)
        drawShiftedCircles(ax,n-1,center,radius*w,w)

def createTree(ax,n,p,h):
    #print('\nN = %d' % n)
    
    if n > 0:
        #print('Current Tree:')
        
        y = p[0,1]
        x = p[0,0]
        
        left = np.array([[x - (2**n), y-h]])
        right = np.array([[x + (2**n), y-h]])                
        
        #print('\nLeft Child: ')
        #print(left)
        #print('\nRight Child: ')
        #print(right)
        
        "Left Child"
        #print('\nAppending and going to left child')
        p = np.append(p, createTree(ax,n-1,left,h), axis=0)
    
        "Parent Node"
        parent = np.array([[p[0,0], p[0,1]]])
        #print('\nAppending parent: ')
        #print(parent)
        p = np.append(p, parent, axis=0)

        "Right Child"
        #print('\nAppending and going to right child')
        p = np.append(p, createTree(ax,n-1,right,h), axis=0)
        
        "Parent"
        parent = np.array([[p[0,0], p[0,1]]])
        #print('\nAppending parent: ')
        #print(parent)
        p = np.append(p, parent, axis=0)
        
        return p
    else:
        "Base Case"
        #print('At leaf returning')
        #print(p)
        return p
    
    
def drawTree(ax,n,p):
    if n == 0:
        #print('At root')
        #print(p)
        return
    else:
        y = -1 * (p[0,1] - (p[0,1] * n))
        p = createTree(ax,n,p,y)
        #print('\nDone with creating tree: ')
        #print(p)
        ax.plot(p[:,0],p[:,1], color='k')
        
        
def drawMultiCirlces(ax,n,center,radius):
    "Base Case"
    #print('\nCurrent Layer: %d' % n)
    if n > 0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        
        ## Recursive Case
        new_rad = radius/3
        Rad_ave = (radius + new_rad) / 2
        #print('Current Radius: %d\nNew Radius: %d\nRadius Average: %d' %(radius,new_rad,Rad_ave))
        tmp_x = center[0]
        #print('\nTemp X Value: %d' % tmp_x)
        tmp_y = center[1]
        #print('Temp Y Value: %d\n' % tmp_y)
        
        c1 = center
        #print('Center Circle 1: ', c1)
        drawMultiCirlces(ax,n-1,c1,new_rad)
        #print('Back from Circle 1')
    
        c2 = np.array([tmp_x - Rad_ave, tmp_y])
        #print('Center Circle 2: ', c2)
        drawMultiCirlces(ax,n-1,c2,new_rad)
        #print('Back from Circle 2')
        
        c3 = np.array([tmp_x, tmp_y + Rad_ave])
        #print('Center Circle 3: ', c3)
        drawMultiCirlces(ax,n-1,c3,new_rad)
        #print('Back from Circle 3')
    
        c4 = np.array([tmp_x + Rad_ave, tmp_y])
        #print('Center Circle 4: ', c4)
        drawMultiCirlces(ax,n-1,c4,new_rad)
        #print('Back from Circle 4')
    
        c5 = np.array([tmp_x, tmp_y - Rad_ave])
        #print('Center Circle 5: ', c5)
        drawMultiCirlces(ax,n-1,c5,new_rad)
        #print('Back from Circle 5')
    else:
        #print('At N = 0, return back to previous call...\n')
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        
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
ax.axis('off')
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
drawShiftedCircles(ax,55,[100,0], 100,.65)
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
p = np.array([[5,5]])
fig, ax = plt.subplots()
ax.axis('on')
ax.set_aspect(1.0)
drawTree(ax,3,p)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_5a.png')

p = np.array([[5,5]])
fig, ax = plt.subplots()
ax.axis('on')
ax.set_aspect(1.0)
drawTree(ax,4,p)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_5b.png')

p = np.array([[5,5]])
fig, ax = plt.subplots()
ax.axis('on')
ax.set_aspect(1.0)
drawTree(ax,7,p)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_5c.png')

## Problem 5
#a
fig, ax = plt.subplots()
ax.axis('on')
ax.set_aspect(1.0)
drawMultiCirlces(ax,1, [100,100], 100)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_6a.png')

fig, ax = plt.subplots()
ax.axis('on')
ax.set_aspect(1.0)
drawMultiCirlces(ax,2, [100,100], 100)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_6b.png')

fig, ax = plt.subplots()
ax.axis('on')
ax.set_aspect(1.0)
drawMultiCirlces(ax,3, [100,100], 100)
plt.show()
fig.savefig('Lab1_Output_Images/lab1_6c.png')