from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Load processed data
df = pd.read_csv("output.csv")

# Convert Date column into datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Combine sales from all regions for each day
daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

# Create Dash app
app = Dash(__name__)

# Create line chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Daily Pink Morsel Sales Before and After Price Increase",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

# Define the layout of the Dash application
app.layout = html.Div([
    html.H1(
        children="Pink Morsel Sales Dashboard",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])
# Run the application
if __name__ == "__main__":
    app.run(debug=True)