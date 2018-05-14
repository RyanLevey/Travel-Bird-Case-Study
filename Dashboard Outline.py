# coding: utf-8

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from pandas import DataFrame
import os

app = dash.Dash(__name__)
server = app.server

# read data for tables (one df per table)
df_performance = pd.read_csv('/Users/ryanc/Desktop/Dash Apps/Travel_Bird/Performance_Market_Factors.csv')
df_quick_cust_data = pd.read_csv("/Users/ryanc/Desktop/Dash Apps/Travel_Bird/Performance_Market_Factors.csv")
df_current_prices = pd.read_csv("/Users/ryanc/Desktop/Dash Apps/Travel_Bird/Adv_Performance.csv")
df_hist_prices = pd.read_csv("/Users/ryanc/Desktop/Dash Apps/Travel_Bird/Historical_ROAS.csv")
df_cust_profile = pd.read_csv('/Users/ryanc/Desktop/Dash Apps/Travel_Bird/Customer_Profile.csv')
df_overall_finance = pd.read_csv("/Users/ryanc/Desktop/Dash Apps/Travel_Bird/Overall_Financial_Performance.csv")
df_cust_profile_canc = pd.read_csv('/Users/ryanc/Desktop/Dash Apps/Travel_Bird/Customer_Profile_Cancel.csv')
df_sourcing = pd.read_csv('/Users/ryanc/Desktop/Dash Apps/Travel_Bird/Returning Customer Data.csv')
df_cust_activity = pd.read_csv('/Users/ryanc/Desktop/Dash Apps/Travel_Bird/New Customer Data.csv')
df_cust_service = pd.read_csv("/Users/ryanc/Desktop/Dash Apps/Travel_Bird/cust_service_data.csv")
df_cust_serv_rev = pd.read_csv("/Users/ryanc/Desktop/Dash Apps/Travel_Bird/cust_serv_rev.csv")
df_avg_returns = pd.read_csv('https://plot.ly/~bdun9/2793.csv')
df_after_tax = pd.read_csv('https://plot.ly/~bdun9/2794.csv')
df_recent_returns = pd.read_csv('https://plot.ly/~bdun9/2795.csv')
df_equity_char = pd.read_csv('https://plot.ly/~bdun9/2796.csv')
df_equity_diver = pd.read_csv('https://plot.ly/~bdun9/2797.csv')
df_expenses = pd.read_csv('https://plot.ly/~bdun9/2798.csv')
df_minimums = pd.read_csv('https://plot.ly/~bdun9/2799.csv')
df_dividend = pd.read_csv('https://plot.ly/~bdun9/2800.csv')
df_realized = pd.read_csv('https://plot.ly/~bdun9/2801.csv')
df_unrealized = pd.read_csv('https://plot.ly/~bdun9/2802.csv')

df_graph = pd.read_csv("https://plot.ly/~bdun9/2804.csv")

# reusable componenets
def make_dash_table(df):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def print_button():
    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

# includes page/full view
def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://fr.travelbird.be/presse/wp-content/uploads/sites/7/2014/12/TravelBird_logo_horizontal512.jpg', height='40', width='160')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Dashboard Outline')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/overview', className="tab first"),

        dcc.Link('Marketing   ', href='/price-performance', className="tab"),

        dcc.Link('Finance   ', href='/portfolio-management', className="tab"),

        dcc.Link('Sourcing   ', href='/fees', className="tab"),

        dcc.Link('Customer Service   ', href='/distributions', className="tab"),

        dcc.Link('Conclusion   ', href='/news-and-reviews', className="tab")

    ], className="row ")
    return menu

## Page layouts
overview = html.Div([  # page 1

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 3

            html.Div([

                html.Div([
                    html.H6('Overview',
                            className="gs-header gs-text-header padded"),

                    html.Br([]),

                    html.P("\
                            This case study serves to illustrate the performance of all departments  \
                            within Travel Bird. The data contained within this report is a synthesis \
                            to develop a data-driven decision for upper management. \
                            Given the data shown below, Travel Bird serves a variety of customers with different taste.\
                            The data presented gives the story of Travel Bird's customers, who we serve to in order to provide the superior traveling experiences. \
                            With that being said, the order in which this Dashboard is presented is customer focoused. The first criteria to be identified is the type of customer (Marketing), \
                            and what type of financial flows we are seeing from the customer (Finance). With this information, it is then possible to identify what partner/supplier relationships  \
                            should be leveraged (Sourcing) and how effecive our partnerships are by means of serving our customers (Customer Service). With this information, it is possible to develop an informed, and a data-driven decision."),

                ], className="six columns"),

                html.Div([
                    html.H6(["Performance/Market Factors"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_performance))
                ], className="six columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6('Number of Offers',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(
                        id = "graph-1",
                        figure={
                            'data': [
                                go.Bar(
                                    x = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
                                    y = ["30", "20", "30", "50", "52", "55", "60", "62"],
                                    marker = {
                                      "color": "rgb(53, 83, 255)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    name = "Number of Offers",
                                    type = "bar"
                                ),
                                go.Bar(
                                    x = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
                                    y = ["7", "3", "7", "12", "15", "16", "17", "18"],
                                    marker = {
                                      "color": "rgb(255, 225, 53)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                        }
                                    },
                                    name = "Number of Countries",
                                    type = "bar"
                                ),
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                bargap = 0.35,
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0228945952895,
                                  "y": -0.189563896463,
                                  "orientation": "h",
                                  "yanchor": "top"
                                },
                                margin = {
                                  "r": 0,
                                  "t": 20,
                                  "b": 10,
                                  "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 340,
                                xaxis = {
                                  "autorange": True,
                                  "range": [-0.5, 4.5],
                                  "showline": True,
                                  "title": "",
                                  "type": "category"
                                },
                                yaxis = {
                                  "autorange": True,
                                  "range": [0, 22.9789473684],
                                  "showgrid": True,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear",
                                  "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

                html.Div([
                    html.H6("Net Revenue",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id="grpah-2",
                        figure={
                            'data': [
                                go.Scatter(
                                    x = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
                                    y = ["10000", "7500", "9000", "10000", "10500", "11000", "14000", "18000"],
                                    line = {"color": "rgb(53, 83, 255)"},
                                    mode = "lines",
                                    name = "Net Revenue (x1000)"
                                )
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                title = "",
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                width = 340,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0277108433735,
                                  "y": -0.142606516291,
                                  "orientation": "h"
                                },
                                margin = {
                                  "r": 20,
                                  "t": 20,
                                  "b": 20,
                                  "l": 50
                                },
                                showlegend = True,
                                xaxis = {
                                  "autorange": True,
                                  "linecolor": "rgb(0, 0, 0)",
                                  "linewidth": 1,
                                  "range": [2010, 2017],
                                  "showgrid": False,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear"
                                },
                                yaxis = {
                                  "autorange": False,
                                  "gridcolor": "rgba(127, 127, 127, 0.2)",
                                  "mirror": False,
                                  "nticks": 4,
                                  "range": [0, 19000],
                                  "showgrid": True,
                                  "showline": True,
                                  "ticklen": 10,
                                  "ticks": "outside",
                                  "title": "$",
                                  "type": "linear",
                                  "zeroline": False,
                                  "zerolinewidth": 4
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row "),

            # Row 5

            html.Div([

                html.Div([
                    html.H6('Customer Profile',
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_cust_profile))
                ], className="six columns"),

                html.Div([
                    html.H6("Customer Satisfaction",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id='graph-3',
                        figure = {
                            'data': [
                                go.Scatter(
                                    x = ["0", "0.18", "0.18", "0"],
                                    y = ["0.2", "0.2", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.2)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "B",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.2", "0.38", "0.38", "0.2", "0.2"],
                                    y = ["0.2", "0.2", "0.6", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.4)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "D",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.4", "0.58", "0.58", "0.4", "0.4"],
                                    y = ["0.2", "0.2", "0.8", "0.6", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.6)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "F",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.6", "0.78", "0.78", "0.6", "0.6"],
                                    y = ["0.2", "0.2", "1", "0.8", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgb(31, 119, 180)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "H",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.8", "0.98", "0.98", "0.8", "0.8"],
                                    y = ["0.2", "0.2", "1.2", "1", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.8)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "J",
                                    showlegend = False
                                ),
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                    {
                                      "x": 0.69,
                                      "y": 0.6,
                                      "font": {
                                        "color": "rgb(31, 119, 180)",
                                        "family": "Raleway",
                                        "size": 30
                                      },
                                      "showarrow": False,
                                      "text": "<b>4</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.0631034482759,
                                      "y": -0.04,
                                      "align": "left",
                                      "font": {
                                        "color": "red",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Not Satisfied</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.92125,
                                      "y": -0.04,
                                      "align": "right",
                                      "font": {
                                        "color": "green",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Satisfied</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    }
                                  ],
                                  autosize = False,
                                  height = 200,
                                  width = 340,
                                  hovermode = "closest",
                                  margin = {
                                    "r": 10,
                                    "t": 20,
                                    "b": 80,
                                    "l": 10
                                  },
                                  shapes = [
                                    {
                                      "fillcolor": "rgb(255, 255, 255)",
                                      "line": {
                                        "color": "rgb(31, 119, 180)",
                                        "width": 4
                                      },
                                      "opacity": 1,
                                      "type": "circle",
                                      "x0": 0.621,
                                      "x1": 0.764,
                                      "xref": "x",
                                      "y0": 0.135238095238,
                                      "y1": 0.98619047619,
                                      "yref": "y"
                                    }
                                  ],
                                  showlegend = True,
                                  xaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.05, 1.05],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.3, 1.6],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row ")

        ], className="subpage")

    ], className="page")


pricePerformance = html.Div([  # page 2 Marketing

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row ``

            html.Div([

                html.Div([
                    html.H6(["Advertising Performance (2017)"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_current_prices))

                ], className="six columns"),

                html.Div([
                    html.H6(["Historical ROAS"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_hist_prices))
                ], className="six columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.H6("Site Visit (x1000)",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id='graph-4',
                        figure={
                            'data': [
                                go.Scatter(
                                    x = df_graph['Date'],
                                    y = df_graph['Vanguard 500 Index Fund'],
                                    line = {"color": "rgb(53, 83, 255)"},
                                    mode = "lines",
                                    name = "Daily Visitors"
                                ),
                                go.Scatter(
                                    x = df_graph['Date'],
                                    y = df_graph['MSCI EAFE Index Fund (ETF)'],
                                    line = {"color": "rgb(255, 225, 53)"},
                                    mode = "lines",
                                    name = "Visitors Who Subscribed"
                                )
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                width = 700,
                                height = 200,
                                font = {
                                    "family": "Raleway",
                                    "size": 10
                                  },
                                 margin = {
                                    "r": 40,
                                    "t": 40,
                                    "b": 30,
                                    "l": 40
                                  },
                                  showlegend = True,
                                  titlefont = {
                                    "family": "Raleway",
                                    "size": 10
                                  },
                                  xaxis = {
                                    "autorange": True,
                                    "range": ["2007-12-31", "2018-03-06"],
                                    "rangeselector": {"buttons": [
                                        {
                                          "count": 1,
                                          "label": "1Y",
                                          "step": "year",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "count": 3,
                                          "label": "3Y",
                                          "step": "year",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "count": 5,
                                          "label": "5Y",
                                          "step": "year"
                                        },
                                        {
                                          "count": 10,
                                          "label": "10Y",
                                          "step": "year",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "label": "All",
                                          "step": "all"
                                        }
                                      ]},
                                    "showline": True,
                                    "type": "date",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": True,
                                    "range": [18.6880162434, 278.431996757],
                                    "showline": True,
                                    "type": "linear",
                                    "zeroline": False
                                  }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="twelve columns")

            ], className="row "),

            # Row 3

            html.Div([

                    html.P("\
                            The two tables above focous primarily on what content the customer is seeing. The metrics given above illustrate how successful the content is in generating website traffic and  \
                            the turn over of the resorces allocated (ROAS) to advertisements. The metrics listed above differentiate from new and current customers. For example, metrics such as New Customer Click Through Rate and Open serve to demonstrate Travel Bird's word-of-mouth. \
                            This is measured by rate of which current customers share the links (That were sent by email) to potential customers. The tables above along with the tables below demonstrate the volume and origin of the web traffic."),


            ], className="row "),

            # Row 4

            html.Div([

                html.Div([

    html.H6('Origin of Web Traffic(x1000)',
            className="gs-header gs-text-header padded"),
    dcc.Graph(
        id = "graph-5",
        figure={
            'data': [
                go.Bar(
                    x = ["Austria", "Belgium", "France", "Germany", "Luxembourg", "The Netherlands", "Norway", "Swedan"],
                    y = ["60", "40", "75", "80", "30", "45", "20", "65"],
                    marker = {
                      "color": "rgb(53, 83, 255)",
                      "line": {
                        "color": "rgb(255, 255, 255)",
                        "width": 2
                      }
                    },
                    name = "From Web Searches",
                    type = "bar"
                ),
                go.Bar(
                    x = ["Austria", "Belgium", "France", "Germany", "Luxembourg", "The Netherlands", "Norway", "Swedan"],
                    y = ["40", "60", "25", "20", "70", "55", "80", "35"],
                    marker = {
                      "color": "rgb(255, 225, 53)",
                      "line": {
                        "color": "rgb(255, 255, 255)",
                        "width": 2
                        }
                    },
                    name = "Email Related Links",
                    type = "bar"
                ),
            ],
            'layout': go.Layout(
                autosize = False,
                bargap = 0.35,
                font = {
                  "family": "Raleway",
                  "size": 9
                },
                height = 200,
                hovermode = "closest",
                legend = {
                  "x": -0.0228945952895,
                  "y": -0.289563896463,
                  "orientation": "h",
                  "yanchor": "botom"
                },
                margin = {
                  "r": 0,
                  "t": 20,
                  "b": 10,
                  "l": 10
                },
                showlegend = True,
                title = "",
                width = 520,
                xaxis = {
                  "autorange": True,
                  "range": [-0.5, 4.5],
                  "showline": True,
                  "title": "",
                  "type": "category"
                },
                yaxis = {
                  "autorange": True,
                  "range": [0, 22.9789473684],
                  "showgrid": True,
                  "showline": True,
                  "title": "",
                  "type": "linear",
                  "zeroline": False
                }
            )
        },
        config={
            'displayModeBar': False
        }
    )
], className=" twelve columns"),

            ], className="row "),

            # Row 5



        ], className="subpage")

    ], className="page")


portfolioManagement = html.Div([ # page 3 Finance

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 3

            html.Div([

                html.Div([
                    html.H6('Finance Overview',
                            className="gs-header gs-text-header padded"),

                    html.Br([]),

                    html.P("\
                            Overall, this section identifies the cost incured from customers and what markets are generating revenue. \
                            In regards to the customer, the data illustrations below show the type of customers whom can be indecisive (and in the long run, can generate expenses), and how hedge against those risk by offering alternative products. \
                            Regarding the finacial flows, the two graphs below identify the markets which market generate the most revenue and the amount of debt incurred to our partners within those markets as well.\
                            By having this understanding, it is posible to identify the bargaining power Travel Bird has in negotiating with its partners in a specific market. This illustration also can be reflective of Travel Bird's relationship with partners as well. \
                            "),

                ], className="six columns"),

                html.Div([
                    html.H6(["Overall Financial Performance"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_overall_finance))
                ], className="six columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6('Order Cancellations',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(
                        id = "graph-6",
                        figure={
                            'data': [
                                go.Bar(
                                    x = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
                                    y = ["5000", "15000", "30000", "20000", "25000", "15000", "14000", "13000"],
                                    marker = {
                                      "color": "rgb(53, 83, 255)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    name = "Number of Order Cancellations",
                                    type = "bar"
                                ),
                                go.Bar(
                                    x = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
                                    y = ["1000", "900", "3000", "8000", "8500", "4000", "4000", "7000"],
                                    marker = {
                                      "color": "rgb(255, 225, 53)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                        }
                                    },
                                    name = "Made Another Purchase",
                                    type = "bar"
                                ),
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                bargap = 0.35,
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0228945952895,
                                  "y": -0.189563896463,
                                  "orientation": "h",
                                  "yanchor": "top"
                                },
                                margin = {
                                  "r": 0,
                                  "t": 20,
                                  "b": 10,
                                  "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 340,
                                xaxis = {
                                  "autorange": True,
                                  "range": [-0.5, 4.5],
                                  "showline": True,
                                  "title": "",
                                  "type": "category"
                                },
                                yaxis = {
                                  "autorange": True,
                                  "range": [0, 22.9789473684],
                                  "showgrid": True,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear",
                                  "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

                html.Div([
                    html.H6("Geographical Revenue (Most Profitable By Continent)",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id="grpah-7",
                        figure={
                            'data': [
                                go.Scatter(
                                    x = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
                                    y = ["10000", "7500", "9000", "10000", "10500", "11000", "14000", "18000"],
                                    line = {"color": "rgb(53, 83, 255)"},
                                    mode = "lines",
                                    name = "Europe (x1000)"
                                ),
                                go.Scatter(
                                    x = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
                                    y = ["15000", "7000", "10000", "10000", "11500", "11000", "13000", "15000"],
                                    line = {"color": "rgb(100, 150, 100)"},
                                    mode = "lines",
                                    name = "Asia (x1000)"
                                ),
                                go.Scatter(
                                    x = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
                                    y = ["7000", "9000", "13000", "16000", "13000", "18000", "18500", "19000"],
                                    line = {"color": "rgb(200, 100, 50)"},
                                    mode = "lines",
                                    name = "South East Asia (x1000)"
                                ),
                                go.Scatter(
                                    x = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
                                    y = ["6000", "8000", "12000", "1000", "15000", "14000", "20000", "14000"],
                                    line = {"color": "rgb(250, 25, 17)"},
                                    mode = "lines",
                                    name = "North America (x1000)"
                                ),


                            ],
                            'layout': go.Layout(
                                autosize = False,
                                title = "",
                                font = {
                                  "family": "Raleway",
                                  "size": 7
                                },
                                height = 290,
                                width = 340,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0277108433735,
                                  "y": -0.142606516291,
                                  "orientation": "h"
                                },
                                margin = {
                                  "r": 20,
                                  "t": 20,
                                  "b": 20,
                                  "l": 50
                                },
                                showlegend = True,
                                xaxis = {
                                  "autorange": True,
                                  "linecolor": "rgb(0, 0, 0)",
                                  "linewidth": 1,
                                  "range": [2010, 2017],
                                  "showgrid": False,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear"
                                },
                                yaxis = {
                                  "autorange": False,
                                  "gridcolor": "rgba(127, 127, 127, 0.2)",
                                  "mirror": False,
                                  "nticks": 4,
                                  "range": [0, 20000],
                                  "showgrid": True,
                                  "showline": True,
                                  "ticklen": 10,
                                  "ticks": "outside",
                                  "title": "$",
                                  "type": "linear",
                                  "zeroline": False,
                                  "zerolinewidth": 4
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row "),

            # Row 5

            html.Div([

                html.Div([
                    html.H6('Customer Profile (Cancellations)',
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_cust_profile_canc))
                ], className="six columns"),

                html.Div([
                    html.H6('Partner Payments (x100000)',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(
                        id = "graph-8",
                        figure={
                            'data': [
                                go.Bar(
                                    x = ["Europe", "Asia", "South East Asia", "North America"],
                                    y = ["57", "40", "32", "15",],
                                    marker = {
                                      "color": "rgb(53, 83, 255)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    name = "Total Partners",
                                    type = "bar"
                                ),

                            ],
                            'layout': go.Layout(
                                autosize = False,
                                bargap = 0.35,
                                font = {
                                  "family": "Raleway",
                                  "size": 9
                                },
                                height = 125,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0228945952895,
                                  "y": -0.2589563896463,
                                  "orientation": "h",
                                  "yanchor": "top"
                                },
                                margin = {
                                  "r": 0,
                                  "t": 20,
                                  "b": 10,
                                  "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 340,
                                xaxis = {
                                  "autorange": True,
                                  "range": [-0.5, 4.5],
                                  "showline": True,
                                  "title": "",
                                  "type": "category"
                                },
                                yaxis = {
                                  "autorange": True,
                                  "range": [0, 22.9789473684],
                                  "showgrid": True,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear",
                                  "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row ")


        ], className="subpage")

    ], className="page")

feesMins = html.Div([  # page 4 Sourcing

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row ``

            html.Div([

                html.Div([
                    html.H6(["Returning Customer Data"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_sourcing))

                ], className="six columns"),

                html.Div([
                    html.H6(["New Customer Data"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_cust_activity))
                ], className="six columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.H6("Number of Regional Partners",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id = "graph-9",
                        figure={
                            'data': [
                                go.Bar(
                                    x = ["Europe", "Asia", "South East Asia", "Africa", "North America", "South America"],
                                    y = ["150", "80", "70", "60", "120", "50"],
                                    marker = {
                                      "color": "rgb(53, 83, 255)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    name = "Hotels",
                                    type = "bar"
                                ),
                                go.Bar(
                                    x = ["Europe", "Asia", "South East Asia", "Africa", "North America", "South America"],
                                    y = ["35", "15", "13", "9", "20", "7"],
                                    marker = {
                                      "color": "rgb(255, 225, 53)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                        }
                                    },
                                    name = "Airlines",
                                    type = "bar"
                                ),
                                go.Bar(
                                    x = ["Europe", "Asia", "South East Asia", "Africa", "North America", "South America"],
                                    y = ["37", "50", "25", "10", "15", "55"],
                                    marker = {
                                      "color": "green",
                                      "line": {
                                        "color": "green",
                                        "width": 2
                                      }
                                    },
                                    name = "Car Rentals",
                                    type = "bar"
                                ),
                                go.Bar(
                                    x = ["Europe", "Asia", "South East Asia", "Africa", "North America", "South America"],
                                    y = ["40", "25", "35", "27", "52", "30"],
                                    marker = {
                                      "color": "red",
                                      "line": {
                                        "color": "red",
                                        "width": 2
                                      }
                                    },
                                    name = "Adventure",
                                    type = "bar"
                                ),
                                go.Bar(
                                    x = ["Europe", "Asia", "South East Asia", "Africa", "North America", "South America"],
                                    y = ["60", "15", "20", "10", "40", "10"],
                                    marker = {
                                      "color": "orange",
                                      "line": {
                                        "color": "orange",
                                        "width": 2
                                      }
                                    },
                                    name = "Luxery",
                                    type = "bar"
                                ),
                                go.Bar(
                                    x = ["Europe", "Asia", "South East Asia", "Africa", "North America", "South America"],
                                    y = ["100", "27", "30", "25", "90", "20"],
                                    marker = {
                                      "color": "rgb(175, 100, 75)",
                                      "line": {
                                        "color": "rgb(200, 125, 100)",
                                        "width": 2
                                      }
                                    },
                                    name = "Tourism",
                                    type = "bar"
                                )
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                bargap = 0.35,
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 400,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0228945952895,
                                  "y": -0.289563896463,
                                  "orientation": "h",
                                  "yanchor": "top"
                                },
                                margin = {
                                  "r": 50,
                                  "t": 20,
                                  "b": 30,
                                  "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 730,
                                xaxis = {
                                  "autorange": True,
                                  "range": [-0.5, 4.5],
                                  "showline": True,
                                  "title": "",
                                  "type": "category"
                                },
                                yaxis = {
                                  "autorange": True,
                                  "range": [0, 22.9789473684],
                                  "showgrid": True,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear",
                                  "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="twelve columns")

            ], className="row "),

            # Row 3

            html.Div([

                    html.P("\
                            The data displayed here indicates how Travel Bird leverages its relationships with its partners to better serve customer needs.  \
                            The two tables above indicate specific behaviors that are trending with current and new customers.  \
                            From this information, it is possible to develop an understanding in order to develop a plan to allocate resources to serve customer needs.\
                            Like the previous section (finance), this section also serves as an tool for negotiating with partners for the fact that it displays an understanding of Travel Bird's customer.\
                            "),


            ], className="row "),

 ], className="subpage")

    ], className="page")

distributions = html.Div([  # page 3 Customer Service

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row ``

            html.Div([

                html.Div([
                    html.H6(["Data: Customer Service"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_cust_service))

                ], className="six columns"),

                html.Div([
                    html.H6(["Revenue Generated From Customer Service(x1000)"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_cust_serv_rev))
                ], className="six columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.H6("Customer Service Request by Location",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id = "graph-10",
                        figure={
                            'data': [
                                go.Bar(
                                    x = ["Austria", "Belgium", "France", "Germany", "Luxembourg", "The Netherlands", "Norway", "Swedan"],
                                    y = ["20000", "50000", "90000", "45000", "15000", "110000", "35000", "40000"],
                                    marker = {
                                      "color": "rgb(53, 83, 255)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    name = "Service Related",
                                    type = "bar"
                                ),
                                go.Bar(
                                    x = ["Austria", "Belgium", "France", "Germany", "Luxembourg", "The Netherlands", "Norway", "Swedan"],
                                    y = ["10000", "27000", "8000", "10000", "90000", "45000", "20000", "30000"],
                                    marker = {
                                      "color": "rgb(255, 225, 53)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                        }
                                    },
                                    name = "Sales Related",
                                    type = "bar"
                                ),
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                bargap = 0.35,
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0228945952895,
                                  "y": -0.389563896463,
                                  "orientation": "h",
                                  "yanchor": "top"
                                },
                                margin = {
                                  "r": 0,
                                  "t": 20,
                                  "b": 10,
                                  "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 530,
                                xaxis = {
                                  "autorange": True,
                                  "range": [-0.5, 4.5],
                                  "showline": True,
                                  "title": "",
                                  "type": "category"
                                },
                                yaxis = {
                                  "autorange": True,
                                  "range": [0, 22.9789473684],
                                  "showgrid": True,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear",
                                  "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="twelve columns")

            ], className="row "),

            # Row 3

            html.Div([

                    html.P("\
                            In this case, customer service is not only necessary to aid with unforseen problems,  \
                            customer service can also serve as a means to generate additional revenue in addition with discovery of complications on the supplier/partner side. \
                            As seen in the finance section, cancelations are followed by a purchase of another product.\
                            The data displayed here is in correspondance with that trend as revenue and sales related calls are increasing. In addition by seeing which region requires more attention to customer service, this also serves as an opertunity to further analyse partner relationships" ),


            ], className="row "),

            # Row 4

            html.Div([

                html.Div([

    html.H6('Sales Generated From Customer Service',
            className="gs-header gs-text-header padded"),
    dcc.Graph(
        id='graph-11',
        figure={
            'data': [
                go.Scatter(
                    x = df_graph['Date'],
                    y = df_graph['Vanguard 500 Index Fund'],
                    line = {"color": "rgb(53, 83, 255)"},
                    mode = "lines",
                    name = "Sales Generated"
                )

            ],
            'layout': go.Layout(
                autosize = False,
                width = 700,
                height = 200,
                font = {
                    "family": "Raleway",
                    "size": 10
                  },
                 margin = {
                    "r": 40,
                    "t": 40,
                    "b": 30,
                    "l": 40
                  },
                  showlegend = True,
                  titlefont = {
                    "family": "Raleway",
                    "size": 10
                  },
                  xaxis = {
                    "autorange": True,
                    "range": ["2007-12-31", "2018-03-06"],
                    "rangeselector": {"buttons": [
                        {
                          "count": 1,
                          "label": "1Y",
                          "step": "year",
                          "stepmode": "backward"
                        },
                        {
                          "count": 3,
                          "label": "3Y",
                          "step": "year",
                          "stepmode": "backward"
                        },
                        {
                          "count": 5,
                          "label": "5Y",
                          "step": "year"
                        },
                        {
                          "count": 10,
                          "label": "10Y",
                          "step": "year",
                          "stepmode": "backward"
                        },
                        {
                          "label": "All",
                          "step": "all"
                        }
                      ]},
                    "showline": True,
                    "type": "date",
                    "zeroline": False
                  },
                  yaxis = {
                    "autorange": True,
                    "range": [18.6880162434, 278.431996757],
                    "showline": True,
                    "type": "linear",
                    "zeroline": False
                  }
            )
        },
        config={
            'displayModeBar': False
        }
    )
], className=" twelve columns"),

            ], className="row "),

            # Row 5



        ], className="subpage")

    ], className="page")

newsReviews = html.Div([  # page 6

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6('Key Points',
                            className="gs-header gs-text-header padded"),
                    html.Br([]),
                    html.P('Marketing: Web traffic is increasing due word of mouth. Click through rate via shared links are increasing'),
                    html.P('Finance: Order Cancelations have been decreasing. This has been followed by customers making another purchase following their cancellation'),
                    html.P('Sourcing: Returning customers are looking for adventures in South East Asia while Newer Customers prefer tourism in Europe. Due to low amount of partners to answer the adventure experience demand in South East Asia, it is needed to consult with new, or current partners.'),
                    html.Br([]),
                    html.P("Customer Service: Customer service is competitive by means of generating revenue. However, the most common service request is for South East Asia. Yet again, issues must be addressed to partners to prevent this problem")
                ], className="six columns"),

                html.Div([
                    html.H6("The Following Steps",
                            className="gs-header gs-table-header padded"),
                    html.P("Need to make more appeal to current customers. Newer customers have a higher click through rate versus older customers."),
                    html.Br([]),
                    html.P("Address issues with partners in South East Asia in regards to customer service. Either find new partners or renegotiate with current partners. "),
                    html.Br([]),
                    html.P("Expand portfolio in regards to adventure experiences for returning customers due to customer base.")
                ], className="six columns"),

            ], className="row ")

        ], className="subpage")

    ], className="page")

noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")



# Describe the layout, or the UI, of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update page
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return overview
    elif pathname == '/price-performance':
        return pricePerformance
    elif pathname == '/portfolio-management':
        return portfolioManagement
    elif pathname == '/fees':
        return feesMins
    elif pathname == '/distributions':
        return distributions
    elif pathname == '/news-and-reviews':
        return newsReviews
    elif pathname == '/full-view':
        return overview,pricePerformance,portfolioManagement,feesMins,distributions,newsReviews
    else:
        return noPage


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True)
