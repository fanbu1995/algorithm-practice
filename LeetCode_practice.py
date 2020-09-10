#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 19:30:14 2020

@author: fan
"""

#%%

## flip the surrounded area problem

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        if len(board) <= 2:
            return 
        
        n = len(board); m = len(board[0])
        
        def mark_noflip(i,j,board,noflip):
            if i<0 or j<0 or i>=n or j >= m:
                return
            
            if board[i][j] == 'X':
                return
            
            if board[i][j] == 'O' and noflip[i][j] == 0:
                noflip[i][j] = 1
                mark_noflip(i+1,j,board,noflip)
                mark_noflip(i-1,j,board,noflip)
                mark_noflip(i,j+1,board,noflip)
                mark_noflip(i,j-1,board,noflip)
            return
        
        def callBFS(board, i, j):
            if i<0 or j<0 or i>=n or j >= m:
                return
            
            if board[i][j] == 'O' and noflip[i][j] == 0:
                board[i][j] = 'X'
                callBFS(board, i+1,j)
                callBFS(board, i-1,j)
                callBFS(board, i,j-1)
                callBFS(board, i,j+1)
                
            return

        
        # 1. go through the border "o"s and mark the un-flippable spots
        noflip = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            mark_noflip(i,0, board, noflip)
            mark_noflip(i,m-1, board, noflip)
        for j in range(n):
            mark_noflip(0,j, board, noflip)
            mark_noflip(n-1,j, board, noflip)
            
        print(noflip)
        
        # 2. go over the board the flip
        for i in range(1, n-1):
            for j in range(1, m-1):
                if board[i][j] == 'O' and noflip[i][j] == 0:
                    callBFS(board, i, j)
                    
                    
        return
    
    
#%%
        
# Town judge problem
        
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        if N == 1:
            if len(trust) == 0:
                return 1
            else:
                return -1
        
        if not trust:
            return -1
        
        trusting = [0 for i in range(N+1)] # discard index 0
        trusted = [0 for i in range(N+1)] # discard index 0
        
        
        for t in trust:
            p1= t[0]; p2 = t[1]
            print(p1,p2)
            trusting[p1] += 1
            trusted[p2] += 1
            
        print(trusting)
        print(trusted)
            
        #no_trusting = [i for i in range (1,N+1) if trusting[i]==0]
        #all_trusted = [i for i in range (1,N+1) if trusting[i]==N-1]
        judge = [i for i in range (1,N+1) if trusting[i]==0 and trusted[i]==N-1]
        
        print(judge)
        
        if len(judge) == 1:
            return judge[0]
        else:
            return -1
        
        
        
#%% implement a Trie
# Word dictionary problem
            
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEndWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if len(word) == 0:
            return
        
        node = self.root
        for l in word:
            node = node.children[l]
        node.isEndWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        def search_node(node, word):
            for i, l in enumerate(word):
                if l not in node.children:
                    if l == '.':
                        for child_l in node.children:
                            if search_node(node.children[child_l], word[i+1:]):
                                return True
                    return False
                else:
                    node = node.children[l]
                
            return node.isEndWord
        
        return search_node(self.root, word)