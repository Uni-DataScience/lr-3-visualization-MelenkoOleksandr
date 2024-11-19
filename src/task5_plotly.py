import numpy as np
import pandas as pd
import plotly.express as px


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
    
    fig.show()
    return fig


df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})
create_interactive_plotly(df)
