
import control
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

num = np.array([3])
den = np.array([4,1])
G = control.tf(num,den)


t,y = control.impulse_response(G)

plt.plot(t,y)
plt.xlabel('Time (s)')
plt.ylabel('Output (Hz)')
plt.show(block=True)
