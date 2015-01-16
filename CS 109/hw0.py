import numpy as np
import matplotlib.pyplot as plt

distance = 10
number_of_points = 3*distance
x = np.linspace(0, distance, number_of_points)  #array of 30 points from 0 to 10
y = np.sin(x)
z = y + np.random.normal(size=number_of_points) * .2
plt.figure(figsize = (14, 6))
plt.plot(x, y, 'ro-', label='A sine wave')
#plt.plot(x, z, 'b-', label='Noisy sine')
plt.legend(loc = 'lower right')
plt.xlabel("X axis")
plt.ylabel("Y axis") 
print "it worked"