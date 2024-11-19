import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    # Descriptive Statistics
    print("Descriptive Statistics:")
    print(df.describe(), "\n")
    
    # Outlier Detection (Box Plot)
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, palette="Set2")
    plt.title('Box Plot for Outlier Detection', fontsize=14)
    plt.xlabel('Variables', fontsize=12)
    plt.ylabel('Value Range', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    
    # Correlation Matrix and Heatmap
    correlation_matrix = df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
    plt.title('Correlation Matrix Heatmap', fontsize=14)
    plt.tight_layout()
    plt.show()


df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)
