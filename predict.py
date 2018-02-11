# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:01:02 2018

@author: Huimin Zhou
"""
import hackathonann

def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

# Sigmoid function: tanh
def sigmoid(x):
    return math.tanh(x)

# Derivated function for y
def dsigmoid(y):
    return 1.0 - y**2

class NN:
    ''' Three-layer back propagation neural network '''
    def __init__(self, ni, nh, no):
        # number of nodes for input, hidden, and output layers
        self.ni = ni + 1 # adding a bias node
        self.nh = nh
        self.no = no

        # Activate all nodes in neural network
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no
        
        # Weights
        self.wi = makeMatrix(self.ni, self.nh)
        self.wo = makeMatrix(self.nh, self.no)
        # Set initial weights as random numbers
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = hackathonann.NN.getweight1()
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = hackathonann.NN.getweight2()

        # Build momentum factor
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)
    def update(self, inputs):
 #      ''' if len(inputs) != self.ni-1:
 #          raise ValueError('Different from # of nodes in input layer!')'''

        # Activate input later
        for i in range(self.ni-1):
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]

        # Activate hidden layer
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoid(sum)

        # Activate output layer
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)

        return self.ao[:]
  
    def test(self, patterns):
        for p in patterns:
            print(p[0], '->', self.update(p[0]))