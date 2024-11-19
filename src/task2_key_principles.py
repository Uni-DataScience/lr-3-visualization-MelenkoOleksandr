import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=data, x='x', y='y', ax=ax, color='purple')
    
    # Add gridlines, labels, and title
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xlabel('X Values', fontsize=12)
    ax.set_ylabel('Y Values', fontsize=12)
    ax.set_title('Scatter Plot of X vs Y', fontsize=14)
    
    # Enhance layout
    plt.tight_layout()
    plt.show()
    return fig


data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})
create_scatter_plot(data)
