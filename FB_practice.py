#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:50:52 2020

@author: fan
"""

# Facebook example interview questions practice

#%%
# 1. spiral array

# when and where to turn
# boundary; how many steps left in current direction

"""
input = 4
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07
"""

## this doesn't work!!
def spiralArray_old(n):
    # 1. simple case
    if n==1:
        res = [[1]]
        printArray(res)
        return
    
    # 2. general case
    res = [[0]*n for i in range(n)]
    
    # the boundaries
    L = 0; R = n-1
    T = 0; D = n-1
    
    # the starting point
    i = j = 0
    num = 1
    
    # current direction
    iDir = 0
    jDir = 1
    
    while num <= n**2:
        # fill in the current number
        
        print(i,j)
        print('L={},R={},T={},D={}'.format(L,R,T,D))
        
        res[i][j] = num
        
        # figure out where to go next
        # 1. check if i or j has reached the boundaries
        ## else, change direction
        if j==R and i==T:
            jDir = 0
            iDir = 1
            T += 1
        if j==R and i==D:
            jDir = -1
            iDir = 0
            R -= 1
        if j==L and i==D:
            jDir = 0
            iDir = -1
            D -= 1
        if j==L and i==T:
            iDir = 0
            jDir = 1
            if i == 0 and j == 0:
                pass
            else:
                L += 1
            
        i += iDir
        j += jDir
        
        num += 1
        
    printArray(res)
    return


## try this one
## This one works!!!
def spiralArray(n):
    # 1. simple case
    if n==1:
        res = [[1]]
        printArray(res)
        return
    
    # 2. general case
    res = [[0]*n for i in range(n)]
    
    # the boundaries
    L = 0; R = n-1
    T = 0; D = n-1
    
    # the starting point
    i = j = 0
    num = 1
    
    # current direction
    iDir = 0
    jDir = 1
    
    while num <= n**2:
        # fill in the current number
        
        #print(i,j)
        #print('L={},R={},T={},D={}'.format(L,R,T,D))
        
        res[i][j] = num
        
        # figure out where to go next
        # check: if the next step is still within the boundaries
        # AND if the next step still is 0
        
        i_next = i + iDir
        j_next = j + jDir
        
        #print('proposed next spot: {}, {}.'.format(i_next, j_next))
        
        if i_next >= T and i_next <= D and j_next >= L and j_next <= R and res[i_next][j_next]==0:
            pass
        else:
            if iDir == 0 and jDir == 1:
                #print('currently going right, next going down')
                iDir = 1
                jDir = 0
            elif iDir == 0 and jDir == -1:
                #print('currently going left, next going up')
                iDir = -1
                jDir = 0
            elif iDir == 1 and jDir == 0:
                #print('currently going down, next going left')
                iDir = 0
                jDir = -1
            else:
                #print('currently going up, next going right')
                iDir = 0
                jDir = 1
                
        i += iDir
        j += jDir
        
        num += 1
        
    printArray(res)
    return
        

def printArray(arr):
    
    if arr is None:
        return
    
    for i in range(len(arr)):
        print(' '.join(map(str, arr[i])))
    
    return
    
    
    





#%%
# 2. look and say sequence

#1
#11
#21
#1211
#111221
#312211
#13112221
#1113213211
#31131211131221
#13211311123113112211

# n=4
# --> n = 3
# ---> n=2 
# prev = '11'
# count = 1; digit = '1'
# i = 1: count = 2
# out = '2' + '1' --> '21'

# prev = '21'
# count = 1; digit = '2'
# i=1: out = '1' + '2' --> '12'
#      count = 1; digit = prev[1] = '1'
# out += '1' + '1' --> out = '12' + '11' --> '1211'



def LookandSay(n):
    if n==1:
        return '1'
    if n==2:
        return '11'
    
    prev = LookandSay(n-1)
    
    out = ''
    
    count = 1
    digit = prev[0]
    
    for i in range(1,len(prev)):
        if digit == prev[i]:
            count += 1
        else:
            out += str(count) + digit
            count = 1
            digit = prev[i]
            
    out += str(count) + digit
    
    return out


#%%
# 3. one-edit distance
    
# length difference > 1: false
# length diff == 1: check insertion and removal
# length diff == 0: check replacement
    

# s1 = 'create'
# s2 = 'crate'
# n1 = 6; n2 = 5

# num_diff = 0
# i = 0,1,2,3,4,5
# i=0: nothing
# i=1: nothing
# i=2: s2 = s2[:2] + s1[2] + s2[2:]
#         = 'cr' + 'e' + 'ate' = 'create'
#      num_diff = 1
# now! s2 = 'create'
# i=3: nothing
# i=4: nothing
# i=5: nothing
    


def OneEditApart(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    
    if abs(n1-n2) > 1:
        return False
    if n1 ==0 and n2==0:
        return False
    
    if n1 < n2:
        temp = s1
        s1 = s2
        s2 = temp
    
    if n2==0 and n1==1:
        return True
    
    # parallel walk-through and check
    if n1 == n2:
        # only allow replacement 
        num_diff = 0
        for i in range(n1):
            if s1[i] != s2[i]:
                num_diff += 1
            if num_diff > 1:
                return False
        return True
    else:
        # only allow insertion or removal
        num_diff = 0
        for i in range(n1):
            if s1[i] != s2[i]:
                # insert s1[i] to ith spot of s2
                s2 = s2[:i] + s1[i] + s2[i:]
                num_diff += 1
            if num_diff > 1:
                return False
        return True
        
    
    
    
    
#%%
# The icecream parlor problem
# find the two indices (1-based index) in arr that sum to m
def icecreamParlor(m, arr):
    if m==0 or len(arr) == 0:
        return
    priceDiffs = dict()
    for i in range(len(arr)):
        if arr[i] in priceDiffs:
            j = priceDiffs[arr[i]]
            return j+1, i+1
        else:
            priceDiffs[m-arr[i]] = i
            
    return
        

#%%    
# check for colorful number
def isColorful(num):
    num = str(num)
    if len(num) <= 1:
        return True
    
    numList = list(map(int,num))
    n = len(numList)
    
    prods = set()
    
    for i in range(n):
        prod = numList[i]
        if prod in prods:
            return False
        prods.add(prod)
        for j in range(i+1,n):
            prod *= numList[j]
            if prod in prods:
                return False
            prods.add(prod)
            
    return True
            
    
#%% 
# quick Sort
# (in place)
def quickSort(x, st, en):
    if en-st <= 1:
        return
    
    q = partition(x, st, en)
    
    quickSort(x, st, q)
    quickSort(x, q+1, en)
    
    return

def partition(x, st, en):
    
    if en-st<=1:
        return
    
    pivot = x[st]
    
    i = st
    for j in range(st+1, en):
        if x[j] < pivot:
            i += 1
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
    
    x[st] = x[i]        
    x[i] = pivot
    
    return i
    
#%%
# Snake and ladders (hacker rank)
from collections import defaultdict, deque

def quickestWayUp(ladders, snakes):
    
    LS = dict()
    # build ladders and snakes
    for l in ladders:
        st, en = l
        LS[st] = en
    for s in snakes:
        st,en = l
        LS[st] = en
        
    # build edges: adjacency list
    adj = defaultdict(list)
    for i in range(1,100):
        # if i is a starting point of ladder/snake
        # no out-degree
        if i in LS:
            continue
        
        for j in range(i+1, min(i+7,101)):
            # if j is a starting point of ladder/snake
            # directly lead to the end point of ladder/snake
            if j in LS:
                adj[i].append(LS[j])
            else:
                adj[i].append(j)
                
    # do BST
    visited = set()
    queue = deque()
    
    # initialize distance vector
    dist = [-1] * 101
    dist[1] = 0
    
    queue.append(1)
    visited.add(1)
    
    while queue:
        orig = queue.pop()
        if orig in visited or orig not in adj:
            continue
        for nei in adj[orig]:
            if nei in visited:
                continue
            dist[nei] = dist[orig] + 1
            queue.append(nei)
            visited.add(nei)
            
    return dist[100]


#%%
def quickestWayUp(ladders, snakes):
    # store ladders and snakes
    LS = dict()
    for l in ladders:
        st, en = l
        LS[st] = en
    for s in snakes:
        st, en = s
        LS[st] = en

    #  build a graph based on ladders and snakes
    adj = dict()
    for i in range(1,100):
        if i in LS:
            # if i is startpoint of L or S, this point doesn't go anywhere
            continue
        # otherwise...
        adj[i] = list()
        for j in range(i+1,min(i+7,101)):
            if j in LS:
                # if j is start point of ladder or snake,
                # put the end point in place of j
                adj[i].append(LS[j])
            else:
                adj[i].append(j)
    
    # BFS on the graph
    visited = set()
    queue = list()
    dist = [-1] * 101 # dist[0] is not used; we need dist[100]
    dist[1] = 0

    queue.insert(0, 1)
    visited.add(1)
    while queue:
        orig = queue.pop()
        if orig not in adj:
            continue
        for c in adj[orig]:
            if c in visited:
                continue
            dist[c] = 1 + dist[orig]
            queue.insert(0, c)
            visited.add(c)

    return dist[100]
        
    
    
            
    
    