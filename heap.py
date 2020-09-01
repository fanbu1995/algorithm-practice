#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:28:09 2020

@author: fan
"""

# implement a heap

#%%
class MinHeap:
    def __init__(self):
        self.data = []
        self.size = 0
    
    def get_left(self, index):
        return index * 2 + 1
    def get_right(self, index):
        return index * 2 + 2
    def get_parent(self, index):
        return (index - 1)//2
    
    def exist_left(self, index):
        return index * 2 + 1 < self.size
    def exist_right(self, index):
        return index * 2 + 2 < self.size
    def exist_parent(self, index):
        return index >= 1
    
    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp
        return
    
    def top(self):
        if self.size == 0:
            return None
        else:
            print(self.data[0]) # also print it out
            return self.data[0]
    
    def insert(self, v):
        self.data.append(v)
        self.size += 1
        
        j = self.size-1
        while self.exist_parent(j) and self.data[self.get_parent(j)] > self.data[j]:
            i = self.get_parent(j)
            self.swap(i, j)
            j = i
        
        return
    
    def settle(self, i):
        # settle element at i to its right spot
        if not self.exist_left(i):
            return
        if not self.exist_right(i) and self.data[i] > self.data[self.get_left(i)]:
            self.swap(i, self.get_left(i))
            i = self.get_left(i)
            self.settle(i)
            return
        if self.data[i] <= self.data[self.get_left(i)] and self.data[i] <= self.data[self.get_right(i)]:
            return
        if self.data[self.get_left(i)] < self.data[self.get_right(i)]:
            self.swap(i, self.get_left(i))
            i = self.get_left(i)
            self.settle(i)
        else:
            self.swap(i, self.get_right(i))
            i = self.get_right(i)
            self.settle(i)
        return
        
    
    def delete(self, v):
        assert v in self.data
        
        i = self.data.index(v)
        
        j = self.size - 1
        
        if i==j:
            # if last element, no swapping needed
            self.data.pop()
            self.size -= 1
        else:
            self.swap(i, j)
            self.data.pop()
            self.size -= 1
            
            self.settle(i)
            
            return
        
    def Print(self):
        print(' '.join(map(str,self.data)))
        
 
#%%       
# try this out

if __name__ == '__main__':
    import random
    
    h = MinHeap()
    for i in random.sample(range(80),20):
        h.insert(i)
        
    h.insert(99)
    h.Print()
    
    v = random.choice(h.data)
    
    h.delete(v)
    h.Print()
    
    h.top()
    h.Print()
            
        
        
        