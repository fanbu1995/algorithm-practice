#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:31:49 2020

@author: fan
"""
#%%
import numpy as np

#%%
# 1. merge sort

def merge(x,y):
    '''
    x: list with length m
    y: list with length n
    '''
    m = len(x); n = len(y)
    if m==0:
        return y
    elif n==0:
        return x
    else:
        z = [0]*(m+n)
        i = 0; j = 0
        for k in range(m+n):
            if i>= m:
                z[k:] = y[j:]
                return z
            elif j>=n:
                z[k:] = x[i:]
                return z
            if x[i] <= y[j]:
                z[k] = x[i]
                i += 1
            else:
                z[k] = y[j]
                j += 1
        return z
    
def mergesort(x):
    n = len(x)
    if n==1:
        return x
    else:
        mid = int(n/2)
        return merge(mergesort(x[:mid]), mergesort(x[mid:]))
    
# try out mergesort: rank a randomly permuated sequence from 1 to 100
if __name__ == '__main__':
    z = np.random.choice(list(range(1,101)), 100, replace=False)
    print(z)
    print(mergesort(z))
    
#%%
# 2. bubble sort (insertion sort)
def insertionSort(x):
    n = len(x)
    if n==1:
        return x
    else:
        for j in range(1,n):
            key = x[j]
            i = j-1
            while x[i] > key and i>=0:
                x[i+1] = x[i]
                i -= 1
            x[i+1] = key
        return x
    
# try out insertion sort: rank a randomly permuated sequence from 1 to 100
if __name__ == '__main__':
    z = np.random.choice(list(range(1,101)), 100, replace=False)
    print(z)
    print(insertionSort(z))
     
 
#%%
# 3. quick sort
    
def quickSort(x, st, en):
    '''
    index i: st <= i < en
    '''
    
    n = en - st
    
    if n <= 1:
        return x
    
    q = partition(x, st, en)
    
    quickSort(x, st, q)
    quickSort(x, q+1, en)

    return x

def partition(x, st, en):
    '''
    use the first element as pivot
    '''

    pivot = x[st]
    
    i = st
    
    for j in range(st+1, en):
        if x[j] < pivot:
            i += 1
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
            
    temp = x[i]
    x[i] = pivot
    x[st] = temp
    
    return i


def rand_quickSort(x, st, en):
    '''
    index i: st <= i < en
    '''
    
    n = en - st
    
    if n <= 1:
        return x
    
    q = rand_partition(x, st, en)
    
    quickSort(x, st, q)
    quickSort(x, q+1, en)

    return x


from random import choice

def rand_partition(x, st, en, verbose=False):
    '''
    select a random element as pivot
    '''
    
    p = choice(range(st,en))
    pivot = x[p]
    
    if verbose:
        print('pivot is {}'.format(pivot))
    
    i = st
    for j in range(0,p):
        if x[j] < pivot:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
            i += 1
    for j in range(p+1,en):
        if x[j] < pivot:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
            i += 1
            
    x[p] = x[i]
    x[i] = pivot
    
    return i
    
    
    
    
if __name__=='__main__':
    z = np.random.choice(list(range(1,101)), 100, replace=False)
    print(z)
    print(quickSort(z, 0, len(z)))
    print(rand_quickSort(z, 0, len(z)))
    
    
    
    
    
    
    
    