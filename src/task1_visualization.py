import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def plot_distribution(data):
    # Count the frequency of each category
    category_counts = Counter(data)
    categories = list(category_counts.keys())
    frequencies = list(category_counts.values())
    
    # Create the bar chart
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(categories, frequencies, color=['blue', 'orange', 'green'])
    
    # Add labels and title
    ax.set_xlabel('Category', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Frequency of Categorical Data', fontsize=14)
    ax.set_xticks(categories)
    
    # Improve layout
    plt.tight_layout()
    plt.show()
    return fig

data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
