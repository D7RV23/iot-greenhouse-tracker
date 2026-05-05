import numpy as np
import matplotlib.pyplot as plt

def create_greenhouse_graph(data_rows):
    # Process data passed from DB script
    temps = [r[0] for r in data_rows]
    hums = [r[1] for r in data_rows]
    
    # Time array in hours (0-24 hour period)
    time = np.array([i for i in range(len(temps))])

    fig = plt.figure(figsize=(8, 6))
    
    plt.subplot(2, 1, 1) # Top plot
    plt.plot(time, temps)
    plt.title("Temperature")
    plt.xlim((0, 24)) # min, max
    plt.ylim((10, 30)) # min, max
    plt.xlabel("Time (hr)")
    plt.ylabel("Temperature (°C)")

    # Humidity:
    plt.subplot(2, 1, 2) # Bottom plot
    plt.plot(time, hums)
    plt.title("Humidity")
    plt.xlim((0, 24)) # min, max
    plt.ylim((0, 100)) # min, max
    plt.xlabel("Time (hr)")
    plt.ylabel("Relative Humidity (%)")

    plt.tight_layout()
    return fig # removed plt.show()