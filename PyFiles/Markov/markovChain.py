import numpy as np

A = np.array([[0.2,0.6,0.3],[0.3,0,0.7],[0.5,0,0.5]])

theta0 = np.array([0,1,0])
i = 0
while i <= 10:
    theta0_ = np.matmul(theta0,A)
    theta0 = np.round(theta0_,5)
    print(theta0)
    print(np.round(np.sum(theta0),5))
    i = i+1
      
