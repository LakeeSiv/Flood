import pandas as pd
import plotly.graph_objects as go

import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import consistant_typical_range_stations
from floodsystem.analysis import sort_risk_level

# get and process the data
stations = build_station_list()
stations = consistant_typical_range_stations(stations)
update_water_levels(stations)

station_list = sort_risk_level(stations)

df = pd.DataFrame(station_list, columns=["name", "coord", "severity"])
df[["lat", "lon"]] = pd.DataFrame(df["coord"].tolist(), index=df.index)

# <------variable styling for marker-------->
def severity_to_color(row):
    if row["severity"] == "S":
        return "red"
    if row["severity"] == "H":
        return "orange"
    if row["severity"] == "M":
        return "yellow"
    if row["severity"] == "L":
        return "green"


def marker(row):
    if row["severity"] == "S":
        return "x"
    elif row["severity"] == "H":
        return "diamond"
    else:
        return "circle"

def marker_size(row):
    if row["severity"] == "S":
        return 15
    elif row["severity"] == "H":
        return 10
    elif row["severity"] == "H":
        return 7.5
    else:
        return 5

df["colour"] = df.apply(severity_to_color, axis=1)
df["marker"] = df.apply(marker, axis=1)
df["marker_size"] = df.apply(marker_size, axis=1)
# <------variable styling for marker--------/>

df["text"] = df["name"] + "<br>" + df["coord"].astype(str)

# app made with Dash

app = dash.Dash(__name__)
server = app.server
app.title = "Flood Warning System"

app.layout = html.Div(
    [
        html.H1("Flood Warning System"), html.A(
            "LakeeSiv(ls914) and fm528", href="https://github.com/cued-ia-computing/flood-fm528-ls914", style={
                "margin": "5", "color": "#9B8E8C"}), html.H4("Webpage by LakeeSiv (ls914)"), dcc.Dropdown(
                    id="select", options=[
                        {
                            "label": "ALL", "value": "ALL"}, {
                                "label": "SEVERE", "value": "S"}, {
                                    "label": "HIGH", "value": "H"}, {
                                        "label": "MEDIUM", "value": "M"}, {
                                            "label": "LOW", "value": "L"},
                                            {
                                            "label": "SEVERE & HIGH", "value": "SH"},
                                            
                                            ], multi=False, value="ALL", style={
                                                "background": "black"}), html.Div(
                                                    id="status_text", children=[]), html.Br(), dcc.Graph(
                                                        id="map", figure={}, style={
                                                            "width": "100vh", "height": "78.5vh"}), ], id="container",)


@app.callback(
    [Output(component_id="status_text", component_property="children"),
     Output(component_id="map", component_property="figure")],
    [Input(component_id="select", component_property="value")]
)
def update_graph(option_slctd):

    if option_slctd == "S":
        text = "SEVERE (red)"
    elif option_slctd == "M":
        text = "MEDIUM (yellow)"
    elif option_slctd == "H":
        text = "HIGH (orange)"
    elif option_slctd == "L":
        text = "LOW (green)"
    elif option_slctd == "SH":
        text = "SEVERE (red), HIGH (orange)"
    else:
        text = "SEVERE (red), HIGH (orange), MEDIUM (yellow), LOW (green)"

    container = f"Severity Shown: {text}"

    dff = df.copy()
    

    if option_slctd != "ALL":
        if option_slctd == "SH":
            dff = dff[(dff["severity"] == "H") | (dff["severity"] == "S")]
        else:
            dff = dff[dff["severity"] == option_slctd]

    fig = go.Figure(data=go.Scattergeo(
        lat=dff["lat"],
        lon=dff["lon"],
        
        text=dff["text"],
        hoverinfo = "text",
        mode="markers",
        marker_color=(dff["colour"]),
        marker_size=dff["marker_size"],
        marker_line_width=1,
        marker_line_color="black",
        marker_symbol=dff["marker"]




    ))

    fig.update_geos(
        center_lon=-3,
        center_lat=54.4,
        scope="europe",
        showcoastlines=True,
        coastlinecolor="black",
        projection_type="equirectangular",

        resolution=50,
        projection_scale=5.5,
        showland=True,
        bgcolor="#1f1f1f",

        landcolor="#9B8E8C",
        showframe=False,
        showlakes=True,
        lakecolor="#C2B2B0",
        showrivers=True,
        rivercolor="#C2B2B0",



    )

    fig.update_layout(
        margin=dict(l=10, r=10, t=0, b=0), paper_bgcolor="#2c2c2c"),

    return container, fig


if __name__ == "__main__":
    app.run_server(debug=True)
