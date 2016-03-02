# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:08:03 2015

@author: patrickkennedy
"""


def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        #print(j)
        while j < len(L):
            #print(j)          
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
    return L
          
def newSort(L):
	for i in range(len(L)-1):
		j = i+1
		while j < len(L):
			if L[i] > L[j]:
				temp = L[i]
				L[i] = L[j]
				L[j] = temp
			j += 1
   
   
   
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        print("i: " + str(i) + ", L[size-i-1]: " + str(L[size-i-1]))        
        if L[size-i-1] == e:
            return True
        if L[size-i-1] < e:
            return False
    return False