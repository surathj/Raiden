# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:11:40 2016

@author: Surath
"""

import numpy as np

class Preprocessor(object):
    def __init__(self, data):
        self.data= data
        
    def normalize(self):
        X = np.array((self.data), dtype=float)
        X = X/100
        return X
        
    def normlize_for_amax(self):
        X = np.array((self.data), dtype=float)
        X = X/np.amax(X, axis=0)
        return X
    
    def transpose(self, data):
        X = np.transpose(data)
        return X