# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:51:49 2020

@author: Bryan Smith

file to test out created classes and functions
"""


from K9_TossnFetch import K9_TossnFetch as k9tf



k9 = k9tf()
k9.load()


dseason='13-18-FLL'
singleseason = k9.get_databyseason(dseason)

print(singleseason.head())
k=input("press close to exit") 


