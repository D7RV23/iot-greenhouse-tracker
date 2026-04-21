import numpy as np
import matplotlib.pyplot as plt

# Temperature:
x = np.array([(i / 60) for i in range(1440)])
y = np.array([0] * 1440)

plt.subplot(2, 1, 1) # Top plot
plt.plot(x,y)
plt.title("Temperature")
plt.xlim((0, 24)) # min, max
plt.ylim((-20, 50)) # min, max
plt.xlabel("Celsius")
plt.ylabel("Time (hr)")

# Humidity:
x = np.array([(i / 60) for i in range(1440)])
y = np.array([0] * 1440)

plt.subplot(2, 1, 2) # Bottom plot
plt.plot(x,y)
plt.title("Humidity")
plt.xlim((0, 24)) # min, max
plt.ylim((0, 100)) # min, max
plt.xlabel("Celsius")
plt.ylabel("Time (hr)")

plt.tight_layout()
plt.show() # edit this to importing the image
