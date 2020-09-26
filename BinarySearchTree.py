#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:13:19 2020

@author: fan
"""

#%% 
# implement a binary search tree

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
# search
def search(node, key):
    if node is None or node.value == key:
        return node
    if key < node.value:
        return search(node.left, key)
    else:
        return search(node.right, key)
    
# search iteratively
def search2(node, key):
    x = node
    while x is not None:
        if key == x.value:
            return x
        if key < x.value:
            x = x.left
        else:
            x = x.right
    return x
        
        
# minValue
def minValue(node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
        
    return node

# maxValue
def maxValue(node):
    if node is None:
        return None
    while node.right is not None:
        node = node.right
        
    return node

# insert
def insert(node, key):
    if node is None:
        return BSTNode(key)
    if key < node.value:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
        
    return node
        
# in-order traversal
def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.value)
    inOrder(node.right)
    return
    
# predecessor
def predecessor(node, key):
    keyNode = search(node, key)
    # if there is left sub-tree:
    # find max of left sub-tree
    if keyNode.left is not None:
        return maxValue(node.left)
    # else: find the first left ancestor
    x = node
    leftAncestor = None
    while x is not None:
        if x.value == key:
            break
        if key < x.value:
            x = x.left
        else:
            leftAncestor = x
            x = x.right
            
    return leftAncestor

# delete
def delete(node, key):
    if node is None:
        return node
    
    if key < node.value:
        node.left = delete(node.left, key)
        
    elif key > node.value:
        node.right = delete(node.right, key)
    
    else:
        if node.right is None:
            temp = node.left
            node = None
            return temp
        elif node.left is None:
            temp = node.right
            node = None
            return temp
        else:
            succ = minValue(node.right)
            node.value = succ.value
            node.right = delete(node.right, succ.value)
            
    return node
            
            
        
        
    

    
            
        
        
    
        