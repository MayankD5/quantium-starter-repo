from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load processed data
df = pd.read_csv("output.csv")

print(df.columns)

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
app.layout = html.Div(

    style={
        "backgroundColor": "#F4F7FC",
        "padding": "30px",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#1E3A8A",
                "marginBottom": "30px"
            }
        ),

        html.Div(

            [

                html.Label(
                    "Select Region",
                    style={
                        "fontWeight": "bold",
                        "fontSize": "18px"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",

                    options=[
                        {"label":" All","value":"all"},
                        {"label":" North","value":"north"},
                        {"label":" South","value":"south"},
                        {"label":" East","value":"east"},
                        {"label":" West","value":"west"},
                    ],

                    value="all",

                    inline=True,

                    style={
                        "marginTop":"10px",
                        "marginBottom":"25px"
                    }

                )

            ]

        ),

        dcc.Graph(
            id="sales-chart",
            figure=fig,
            style={
                "backgroundColor":"white",
                "padding":"20px",
                "borderRadius":"15px",
                "boxShadow":"0px 4px 12px rgba(0,0,0,0.15)"
            }
        )

    ]
)
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    # Filter data based on selected region
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    # Combine sales by date
    daily_sales = filtered_df.groupby("Date", as_index=False)["Sales"].sum()

    # Create updated line chart
    fig = px.line(

    daily_sales,

    x="Date",

    y="Sales",

    title="Pink Morsel Sales Over Time",

    markers=False
)

    fig.update_layout(

    title={
        "text":"Pink Morsel Sales Over Time",
        "x":0.5
    },

    plot_bgcolor="white",

    paper_bgcolor="white",

    font=dict(
        family="Arial",
        size=15
    ),

    xaxis_title="Date",

    yaxis_title="Total Sales",

    hovermode="x unified"

)

    return fig

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
    