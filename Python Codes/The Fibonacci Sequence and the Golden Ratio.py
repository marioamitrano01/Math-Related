import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math

class FibonacciAnalyzer:
    
    def __init__(self):
        self.sequence = []
        self.golden_ratio = (1 + math.sqrt(5)) / 2  
    
    def generate_sequence(self, n):
        if n <= 0:
            return []
        
        self.sequence = [0, 1]
        
        for i in range(2, n):
            next_number = self.sequence[i-1] + self.sequence[i-2]
            self.sequence.append(next_number)
            
        return self.sequence
    
    def visualize_sequence_growth(self):
        if not self.sequence or len(self.sequence) < 10:
            self.generate_sequence(20)
        
        fig = go.Figure()
        
        indices = list(range(len(self.sequence)))
        
        fig.add_trace(
            go.Bar(
                x=indices,
                y=self.sequence,
                name='Fibonacci Numbers',
                marker_color='rgba(55, 83, 109, 0.7)',
                hovertemplate='F(%{x}) = %{y}<extra></extra>'
            )
        )
        
        x_trend = np.linspace(0, len(self.sequence)-1, 100)
        y_trend = [(self.golden_ratio**x / math.sqrt(5)) for x in x_trend]
        
        fig.add_trace(
            go.Scatter(
                x=x_trend,
                y=y_trend,
                mode='lines',
                line=dict(color='red', width=2, dash='dash'),
                name=f'φⁿ/√5 ≈ {self.golden_ratio:.4f}ⁿ/√5'
            )
        )
        
        fig.update_layout(
            title={
                'text': 'Exponential Growth of Fibonacci Sequence',
                'font': {'size': 24, 'family': 'Arial', 'color': '#333333'}
            },
            xaxis=dict(
                title='Index (n)',
                titlefont=dict(size=16),
                gridcolor='lightgray'
            ),
            yaxis=dict(
                title='Fibonacci Number F(n)',
                titlefont=dict(size=16),
                type='log',  
                gridcolor='lightgray'
            ),
            plot_bgcolor='white',
            hoverlabel=dict(
                bgcolor="white",
                font_size=16
            ),
            legend=dict(
                x=0.01,
                y=0.99,
                bgcolor='rgba(255, 255, 255, 0.7)',
                bordercolor='rgba(0, 0, 0, 0.5)',
                borderwidth=1
            ),
            height=600,
            width=900
        )
        
        fig.add_annotation(
            x=len(self.sequence)*0.7,
            y=self.sequence[-1]*0.5,
            text="The Fibonacci sequence<br>grows exponentially",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='black',
            ax=-80,
            ay=-50,
            bordercolor='black',
            borderwidth=2,
            borderpad=4,
            bgcolor='white',
            opacity=0.8
        )
        
        return fig
    
    def visualize_golden_ratio(self):
        if not self.sequence:
            self.generate_sequence(20)
        
        ratios = []
        for i in range(1, len(self.sequence)):
            if self.sequence[i-1] != 0: 
                ratios.append(self.sequence[i] / self.sequence[i-1])
            else:
                ratios.append(None)
        
        fig = go.Figure()
        
        indices = list(range(1, len(self.sequence)))
        valid_indices = []
        valid_ratios = []
        
        for i, ratio in zip(indices, ratios):
            if ratio is not None:
                valid_indices.append(i)
                valid_ratios.append(ratio)
        
        fig.add_trace(
            go.Scatter(
                x=valid_indices,
                y=valid_ratios,
                mode='lines+markers',
                name='F(n)/F(n-1)',
                marker=dict(
                    size=8,
                    color='rgba(55, 126, 184, 0.8)',
                    line=dict(width=1, color='DarkSlateGrey')
                ),
                line=dict(color='rgba(55, 126, 184, 0.8)'),
                hovertemplate='n=%{x}<br>F(%{x})/F(%{x}-1)=%{y:.8f}<extra></extra>'
            )
        )
        
        fig.add_trace(
            go.Scatter(
                x=[1, len(self.sequence)],
                y=[self.golden_ratio, self.golden_ratio],
                mode='lines',
                line=dict(color='gold', width=2, dash='dash'),
                name=f'Golden Ratio (φ ≈ {self.golden_ratio:.8f})'
            )
        )
        
        fig.update_layout(
            title={
                'text': 'Convergence to the Golden Ratio',
                'font': {'size': 24, 'family': 'Arial', 'color': '#333333'}
            },
            xaxis=dict(
                title='Index (n)',
                titlefont=dict(size=16),
                gridcolor='lightgray'
            ),
            yaxis=dict(
                title='Ratio F(n)/F(n-1)',
                titlefont=dict(size=16),
                gridcolor='lightgray',
                range=[1, 2.2]  
            ),
            plot_bgcolor='white',
            hoverlabel=dict(
                bgcolor="white",
                font_size=16
            ),
            legend=dict(
                x=0.01,
                y=0.99,
                bgcolor='rgba(255, 255, 255, 0.7)',
                bordercolor='rgba(0, 0, 0, 0.5)',
                borderwidth=1
            ),
            height=600,
            width=900
        )
        
        fig.add_annotation(
            x=10,
            y=self.golden_ratio + 0.1,
            text="Consecutive ratios converge<br>to the Golden Ratio φ ≈ 1.618...",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='black',
            ax=0,
            ay=-40,
            bordercolor='black',
            borderwidth=2,
            borderpad=4,
            bgcolor='white',
            opacity=0.8
        )
        
        return fig


def main():
    print("Fibonacci Sequence")
    
    fib = FibonacciAnalyzer()
    
    try:
        terms = int(input("Enter the number of Fibonacci terms to generate: "))
        
        if terms <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    sequence = fib.generate_sequence(terms)
    
    print("\nFibonacci Sequence:")
    print(f"{'Index (n)':<10}|{'F(n)'}")
    print("-" * 10 + "+" + "-" * 20)
    
    for i, num in enumerate(sequence):
        print(f"{i:<10}|{num}")
    
    print("\nCreating mathematically accurate visualizations...")
    
    growth_fig = fib.visualize_sequence_growth()
    growth_fig.write_html("fibonacci_exponential_growth.html")
    print("Exponential growth visualization saved to 'fibonacci_exponential_growth.html'")
    
    ratio_fig = fib.visualize_golden_ratio()
    ratio_fig.write_html("fibonacci_golden_ratio.html")
    print("Golden ratio visualization saved to 'fibonacci_golden_ratio.html'")
    
    try:
        print("\nDisplaying exponential growth visualization in browser...")
        growth_fig.show()
        
        print("\nDisplaying golden ratio visualization in browser...")
        ratio_fig.show()
    except Exception as e:
        print(f"Could not display figures in browser: {e}")
        print("HTML files have been saved and can be opened manually.")
    
    print("\nAnalysis complete! All visualizations have been saved as HTML files.")


if __name__ == "__main__":
    main()
