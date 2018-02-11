import math
import random

random.seed(0)

# Generate random number between (a,b)
def rand(a, b):
    return (b-a)*random.random() + a

# Generate matrix [I,J]
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
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)

        # Build momentum factor
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)

    def update(self, inputs):
 #      if len(inputs) != self.ni-1:
 #      raise ValueError('Different from # of nodes in input layer!')'''

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

    def backPropagate(self, targets, N, M):
        ''' Back propagation '''
        if len(targets) != self.no:
            raise ValueError('Different from # of nodes in output layer!')

        # calculate error for output layer
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k]-self.ao[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error

        # calculate error for hidden layer
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error

        # Update weights for output layer
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M*self.co[j][k]
                self.co[j][k] = change
                #print(N*change, M*self.co[j][k])

        # Update weights for input layer
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change

        # Calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k]-self.ao[k])**2
        return error

    def test(self, patterns):
        for p in patterns:
            return self.update(p[0])

    def weights(self):
        print('Weights of input layer:')
        for i in range(self.ni):
            print(self.wi[i])

        print('Weights of output layer:')
        for j in range(self.nh):
            print(self.wo[j])

    def train(self, patterns, iterations=1000, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 100 == 0:
                return 'error %-.5f' % error


    def demo(self, avgImpact, numArticles, stkChange, testOrTrain):
        # a demo
        if testOrTrain == True:
            test = [
                [[avgImpact,numArticles], [stkChange]]
            ]
            # test data with testing pattern
            print(self.test(test))

        else:
            training = [
            [[avgImpact,numArticles], [stkChange]]
            ]
            print(self.train(training))

    def finalTest(self, avgImpact, numArticles):
        predict = [
            [[avgImpact, numArticles], [0]]
            ]
        return self.test(predict)




#if __name__ == '__main__':
    #demo()
