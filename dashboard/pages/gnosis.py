import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
import plotly_express as px
from utils.gnosis_safe_data_retrieval import txDescending

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Gnosis")
st.sidebar.header("Gnosis")
st.write(
    """Plot data from Gnosis Subgraph on The Graph"""
)

# Load gnosis data from utils
df = txDescending()

# Download CSV button
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

st.download_button(
   "Download Gnosis Subgraph Data (.csv)",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
wallet_address, destination_address, operation = "", "", ""
temp_df = df

def clear_multi():
    st.session_state.multiselect = []
    return

with st.expander("Advanced Settings"):
    wallet_address = st.multiselect(
                    'Show wallet addresses',
                    np.unique(temp_df['id'].values),
                    key="multiselect")
    # destination_address = st.multiselect(
    #                 'Show destination addresses',
    #                 np.unique(temp_df['destination'].values),
    #                 key="multiselect")
    st.button("Reset", on_click=clear_multi)

if(len(wallet_address) != 0): temp_df = temp_df[df['id'].isin(wallet_address)]
#if(len(destination_address) != 0): temp_df = temp_df[df['destination'].isin(destination_address)]

#temp_df = df
#if(wallet_address != ""): temp_df = df[df['id'] == wallet_address]

def interactive_plot(df):
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('X-axis', options=df.columns)
    y_axis_val = col2.selectbox('Y-axis', options=df.columns)

    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)

interactive_plot(temp_df)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

#progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")