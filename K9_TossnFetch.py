# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:33:41 2020

@author: Bryan Smith (brsm11)
This is a class for reading and manipulating data
from the k9 toss and fetch league.


Class Name:
    K9_TossnFetch
    
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog

class K9_TossnFetch():
    

    
    
    
    
    
    
    def __init__(self, file=None):
        self.file=file
        
        
    def load(self,file=None):
        """loads a csv file containing K9 toss and fetch data
            returns a pandas datafram containing entire file"""
        if file == None:
            if self.file==None:
                file=filedialog.askopenfilename()
        elif not self.file==None:
            file = self.file
        if file == '':
            print('wrong file path')
            #add raise error
        self.data = pd.read_csv(file)
        return
        
    def get_databyseason(self,season):
        '''This function can be used to find the total number of unique players in a given season
        It takes the requested  season in form 001-YYYY-SEASON and the dataFrame containing 
        the season information.
        This function returns a dataframe containg all info for the given season'''
    
        dfseason = self.data[self.data['Season']==season]
        return dfseason
        
    