import numpy as np
from matplotlib import pyplot as plt
import Trainer as tr
import Trainer_Mod as trm
import Preprocessor as pp
import pandas as pd
import time
from tkinter import *

ax = plt.subplots()

class Neural_Network(object):
    def __init__(self):        
        #Define Hyperparameters
        self.inputLayerSize = 4
        self.outputLayerSize = 1
        self.hiddenLayerSize = 10
        
        #Weights (parameters)
        #W1 = layer 1 weights
        #W2 = Layer 2 weights
        self.W1 = np.random.randn(self.inputLayerSize,self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize)
        
        #learning coefficient - bias
        self.bias = 0.0003        
        
        #regularaization parameter
        self.Lambda = 0.0001
        
    def feed_forward(self, X):
        #Propogate inputs though network
        #z2 = Layer 2 activation
        #a2 = Layer 2 activity
        #z3 = Layer 3 activation
        #yHAt = Actual output
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3) 
        return yHat
        
    def sigmoid(self, z):
        #Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))
    
    def sigmoidPrime(self,z):
        #Gradient/Derivative of sigmoid
        return np.exp(-z)/((1+np.exp(-z))**2)
    
    def costFunction(self, X, y):
        #Compute cost for given X,y, use weights already stored in class.
        #X = Input matrix
        #y = Desired output
        #J = Cost
        self.yHat = self.feed_forward(X)
        J = 0.5*sum((y-self.yHat)**2)/X.shape[0] + (self.Lambda/2)*(sum(self.W1**2)+sum(self.W2**2))
        #print("Cost: ", J)
        return J
        
    def costFunctionPrime(self, X, y):
        #Compute derivative with respect to W and W2 for a given X and y:
        self.yHat = self.feed_forward(X)
        #delta3 = 
        #dJdW2 = Derivative of Cost J with respect to layer 2 weights W2
        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)/X.shape[0] + self.Lambda*self.W2
        #dJdW1 = Derivative of Cost J with respect to layer 1 weights W1
        delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)/X.shape[0] + self.Lambda*self.W1  
        
        return dJdW1, dJdW2
        
    #Helper Functions for interacting with other classes:
    def getParams(self):
        #Get W1 and W2 unrolled into vector:
        params = np.concatenate((self.W1.ravel(), self.W2.ravel()))
        return params
    
    def setParams(self, params):
        #Set W1 and W2 using single paramater vector.
        W1_start = 0
        W1_end = self.hiddenLayerSize * self.inputLayerSize
        self.W1 = np.reshape(params[W1_start:W1_end], (self.inputLayerSize , self.hiddenLayerSize))
        W2_end = W1_end + self.hiddenLayerSize*self.outputLayerSize
        self.W2 = np.reshape(params[W1_end:W2_end], (self.hiddenLayerSize, self.outputLayerSize))
        
    def computeGradients(self, X, y):
        dJdW1, dJdW2 = self.costFunctionPrime(X, y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))
        
            
def computeNumericalGradient(N, X, y):
        paramsInitial = N.getParams()
        numgrad = np.zeros(paramsInitial.shape)
        perturb = np.zeros(paramsInitial.shape)
        e = 1e-4
        print("calculating loss")
        for p in range(len(paramsInitial)):
            #Set perturbation vector
            perturb[p] = e
            N.setParams(paramsInitial + perturb)
            loss2 = N.costFunction(X, y)
            
            N.setParams(paramsInitial - perturb)
            loss1 = N.costFunction(X, y)

            #Compute Numerical Gradient
            numgrad[p] = (loss2 - loss1) / (2*e)

            #Return the value we changed to zero:
            perturb[p] = 0
            
        #Return Params to original value:
        N.setParams(paramsInitial)

        return numgrad
        
def read_dataset_from_csv(path):
    raiden_dataset = []
    dataset = pd.read_csv(path, parse_dates=True)
    df = pd.DataFrame(dataset, columns = ['health', 'score', 'class_packs', 'out_of_bounds'])
    for i in range(0, len(df)):
        record = list(df.iloc[i])
        raiden_dataset.append(record)
    return raiden_dataset
    
def read_dataset_class_from_csv(path):
    raiden_dataset_classes = []
    dataset = pd.read_csv(path, parse_dates=True)
    df = pd.DataFrame(dataset, columns = ['result_rate'])
    for i in range(0, len(df)):
        record = list(df.iloc[i])
        raiden_dataset_classes.append(record)
    return raiden_dataset_classes
    
def just_print():
    st = "lalalalala"
    return st

def Agent(): 
   #X = input matrix
    #X = np.array(([[3,5], [5,1], [10,2]]), dtype=float)
    #y = desired output
    #y = np.array([[75], [82], [93]], dtype=float)
    print("inside agent")
    #initializing neural network
    nn = Neural_Network()
    #initialiing Trainer
    T = tr.trainer(nn)
    #training data
    train_X = read_dataset_from_csv('F:\\Projects\\FYP\\ANN\\training_set.csv')
    train_y = read_dataset_class_from_csv('F:\\Projects\\FYP\\ANN\\training_set.csv')
    X = np.array((train_X), dtype=float)
    y = np.array((train_y), dtype=float)
    np.transpose(X)
    np.transpose(y)
    
    
    #Normalization
    X = X/np.amax(X, axis=0)
    y = y/100
    
    
    
    #validation data
    val_X = read_dataset_from_csv('F:\\Projects\\FYP\\ANN\\validation_set.csv')
    val_y = read_dataset_class_from_csv('F:\\Projects\\FYP\\ANN\\validation_set.csv')
    vx = np.array((val_X), dtype=float)
    vy = np.array((val_y), dtype=float)
    np.transpose(vx)
    np.transpose(vy)
    
    vx = vx/np.amax(vx, axis=0)
    vy = vy/100
    
    
    
    T.train(X,y, vx, vy)
    #yhat = nn.feed_forward(vx)
    
    
    
    test_X = read_dataset_from_csv('F:\\Projects\\FYP\\ANN\\test_set.csv')
    #test_y = read_dataset_class_from_csv('F:\\Projects\\FYP\\ANN\\test_set.csv')
    tx = np.array((test_X), dtype=float)
    #ty = np.array((test_y), dtype=float)
    np.transpose(tx)
    #np.transpose(ty)
    
    tx = tx/np.amax(tx, axis=0)
    #ty = ty/100
    
    nx = np.array(([[90.9, 75.4, 5, 0]]), dtype=float)
    np.transpose(nx)
    nx = nx/np.amax(nx, axis=0)

    #T.train(vx, vy, tx, ty)
    that = nn.feed_forward(tx)
    #yhat = nn.feed_forward(nx)
    print(that, " :that")
    return that
    #print("yhat: ", yhat)
    #return that
    #print(T.testJ)
    
    #plt.plot(T.J)
    #plt.plot(T.testJ)
    #plt.grid(1)
    #plt.xlabel('Iterations')
    #plt.ylabel('Cost')
    

if __name__ == '__main__':
    
    root = Tk()
    lable_data = Label(root, text="Data")
    entry_data = Entry(root, width=50)
    e = entry_data.insert(0, "F:\\Projects\\FYP\\ANN\\test_set.csv")
    
    
    lable_output = Label(root, text="Output")
    entry_output = Entry(root, width=50)
    
    def run_ann():
        print("inside run")
        yhat = Agent()
        entry_output.insert(0, yhat)

    button_run = Button(root, text="Run ANN", fg="red", command=run_ann)
    lable_data.grid(row=0, sticky=E)
    entry_data.grid(row=0, column=1)
    button_run.grid(row=1, column=1)
    lable_output.grid(row=2)
    entry_output.grid(row=2, column=1)
    
    root.mainloop()
#Agent()