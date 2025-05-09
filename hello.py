import numpy as np
import pandas as pd
from preswald import Workflow, text, table, plotly, sidebar, connect, get_df,query
import plotly.express as px

# Create a workflow instance
workflow = Workflow()

@workflow.atom()
def load_data():
    #load data
    connect()
    df = get_df('sample_csv')
    return df

@workflow.atom(dependencies=["load_data"])
def analyze_data(load_data):
    df = load_data
    
   #QUERY data
    filtered_df = df[df['RANK'] <= 30]

    #build UI
    text("# My Data Analysis App")
    text("Top 30 Students")
    table(filtered_df, title="Filtered Data")

    #visualize
    fig = px.scatter(df,x="RANK", y="TOTAL SCORE (OUT of 100)",  color="Specialisation")
    plotly(fig)

   

# Execute the workflow
workflow.execute()
