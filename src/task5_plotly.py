import numpy as np
import pandas as pd
import plotly.express as px
import os

def create_interactive_plotly(df):
    fig = px.scatter(
        df, 
        x='x', 
        y='y', 
        title='Interactive Scatter Plot',
        labels={'x': 'X Values', 'y': 'Y Values'},
        color=df['y'],
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        title_font_size=16,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        legend_title="Color Scale",
    )
    
    os.makedirs(os.path.dirname('plots/interactive_scatter_plot.html'), exist_ok=True)
    fig.write_html('plots/interactive_scatter_plot.html')
    print(f"Interactive plot saved to plots/interactive_scatter_plot.html")
    
    fig.show()
    return fig


df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})
create_interactive_plotly(df)
