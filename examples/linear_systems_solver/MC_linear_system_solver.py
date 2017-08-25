'''

to solve cx = b, which is equal to x=ax+b in this code, thus c=I-a

the test matrix is from this slides which presents this Monte Carlo Solvers: http://math.nist.gov/mcsd/Seminars/2014/2014-11-04-Li-presentation.pdf;

the demonstration of this method which shows that the variable selecte in this method is un a unbiased estimator of solution x, this demonstration is given by this article:

http://www.sid.ir/en/VEWSSID/J_pdf/134520050501.pdf


'''
import numpy as np
import random

NUM_SAMPLING = 1000 #sampling number

a = np.array([[0.1,0.45,0.225], [-0.15,0.1,-0.3],[-0.18,0.36,0.1]])
I = np.array([[1.,0.,0.], [0.,1.,0.],[0.,0.,1.]])
suma =  np.array([0.775,0.55,0.64]) #sum of each row of matrix a
p = np.array([[0.129032, 0.580645,0.290323], [0.272727,0.181818,0.545455],[0.28125,0.5625,0.15625]])
c = I-a
#print c
b = np.array([0.225,1.35,0.72])
x = np.linalg.solve(c, b) #exact solver proposed by Numpy
print '\n','Exact solution by Numpy Solver is:',x,'\n' #exact solution by Numpy Solver

estim_x = [0]*3
for i in range(0,3): #index means the position index in array like b and x
    index = i
    SUM = 0
    for _ in range(NUM_SAMPLING):
        
        e = 0.001
        W = 1
        X = 0

        X = X + W*b[index]

        while(abs(W)>e):
            v = random.uniform(0,1) #column random work accept probality
            j = 0 # column index
            sm = p[index][j]
            while(v > sm):
                j =j+1
                sm = sm + p[index][j]
            W = W * np.sign(a[index][j])*suma[index]
            X = X + W * b[j]
            #print X
            index =j
        SUM = SUM + X
    #print i
    estim_x[i] = SUM / NUM_SAMPLING
print 'Approximate solution by Monte Carlo is:', estim_x,'\n'
print '---------------Evaluation the accuration of resolution by Monte Carlo method-------------\n'
print '               True Residual = ||Ax-b|| = ', np.linalg.norm(c.dot(estim_x) - b),'\n'
print '-----------------------------------------------------------------------------------------\n'
