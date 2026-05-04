import numpy as np
import matplotlib.pyplot as plt

def create_greenhouse_graph(data_rows):
    # Process data passed from DB script
    temps = [r[0] for r in data_rows]
    hums = [r[1] for r in data_rows]
    
    # Temperature
    x = np.array([(i / 60) for i in range(len(temps))])

    fig = plt.figure(figsize=(8, 6))
    
    plt.subplot(2, 1, 1) # Top plot
    plt.plot(x, temps)
    plt.title("Temperature")
    plt.xlim((0, 24)) # min, max
    plt.ylim((-20, 50)) # min, max
    plt.xlabel("Celsius")
    plt.ylabel("Time (hr)")

    # Humidity:
    plt.subplot(2, 1, 2) # Bottom plot
    plt.plot(x, hums)
    plt.title("Humidity")
    plt.xlim((0, 24)) # min, max
    plt.ylim((0, 100)) # min, max
    plt.xlabel("Celsius")
    plt.ylabel("Time (hr)")

    plt.tight_layout()
    return fig # removed plt.show()