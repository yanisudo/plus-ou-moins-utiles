import plotly.express as px
import pandas as pd

def create_interactive_plot(data):
    fig = px.bar(data, x='Fruit', y='Amount', color='City', barmode='group')
    fig.show()

if __name__ == "__main__":
    data = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })
    create_interactive_plot(data)
