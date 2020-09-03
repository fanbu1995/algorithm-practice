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
        
    
    
    
    
    
            
        
    
    
    

