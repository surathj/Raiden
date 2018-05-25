# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 03:55:18 2016

@author: Surath
"""
from scipy import optimize

class trainer(object):
    def __init__(self, N):
        #Make Local reference to network:
        self.N = N
        self.J = []
        self.testJ = []
        
    def callbackF(self, params):
        self.N.setParams(params)
        self.J.append(self.N.costFunction(self.X, self.y))
        
    def costFunctionWrapper(self, params, X, y):
        self.N.setParams(params)
        cost = self.N.costFunction(X, y)
        grad = self.N.computeGradients(X,y)
        
        return cost, grad
        
    def train(self, X, y):
        #Make an internal variable for the callback function:
        self.X = X
        self.y = y
        

        #Make empty list to store training costs:
        self.J = []
        
        params0 = self.N.getParams()
        

        options = {'maxiter': 100000, 'disp' : True}
        
        _res = optimize.fmin_l_bfgs_b(self.costFunctionWrapper, params0, fprime=None, args=(X,y), approx_grad=0, \
                                      bounds=None, m=10, factr=10000000.0, pgtol=1e-05, epsilon=1e-08, \
                                      iprint=-1, maxfun=15000, maxiter=15000, disp=None, callback=self.callbackF)
        '''_res = optimize.minimize(self.costFunctionWrapper, params0, jac=True, method='BFGS', \
                                 args=(X, y), options=options, callback=self.callbackF)'''

        #self.N.setParams(_res.x)
        self.optimizationResults = _res