import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(data, color='blue', label='1D Line Plot')
    
    ax.set_xlabel('Index', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_title('1D Line Plot', fontsize=14)
    
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()
    return fig


def plot_2d(x, y):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(x, y, color='green', alpha=0.7, label='2D Scatter Plot')
    
    ax.set_xlabel('X Values', fontsize=12)
    ax.set_ylabel('Y Values', fontsize=12)
    ax.set_title('2D Scatter Plot', fontsize=14)
    
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()
    return fig


def plot_3d(x, y, z):
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=z, cmap='viridis', label='3D Scatter Plot')
    
    ax.set_xlabel('X Values', fontsize=12)
    ax.set_ylabel('Y Values', fontsize=12)
    ax.set_zlabel('Z Values', fontsize=12)
    ax.set_title('3D Scatter Plot', fontsize=14)
    
    ax.legend()
    
    plt.tight_layout()
    plt.show()
    return fig


x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
