import matplotlib.pyplot as plt
import numpy as np

def initial_plot():
    """
    Generates a scatter plot of 4 different points.
    """
    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]
    plt.scatter(x, y, color='blue', label='Points')
    plt.title("Scatter Plot of 4 Points")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_cosinus_with_labels():
    """
    Generates a cosine function plot with all labels.
    """
    x = np.linspace(0, 10, 100)  # 100 data points between 0 and 10
    y = np.cos(x)
    plt.plot(x, y, label='Cosine', color='green')
    plt.title("Cosine Function")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_cosinus_and_sinus_with_labels():
    """
    Generates a plot of both cosine and sine functions with all labels.
    """
    x = np.linspace(0, 10, 100)  # 100 data points between 0 and 10
    y_cos = np.cos(x)
    y_sin = np.sin(x)
    plt.plot(x, y_cos, label='Cosine', color='green')
    plt.plot(x, y_sin, label='Sine', color='red')
    plt.title("Cosine and Sine Functions")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    print("Testing initial_plot()...")
    initial_plot()
    
    print("Testing plot_cosinus_with_labels()...")
    plot_cosinus_with_labels()
    
    print("Testing plot_cosinus_and_sinus_with_labels()...")
    plot_cosinus_and_sinus_with_labels()