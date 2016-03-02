# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:08:54 2015

@author: patrickkennedy
"""

def fibGen():
    fibn_1 = 1
    fibn_2 = 0
    
    while True:
        next = fibn_1 + fibn_2
    
        yield next
    
        fibn_2 = fibn_1
        fibn_1 = next
        
    
    