import streamlit as st
import time
import numpy as np
from utils.airstack_data_retrieval import *

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
# st.write(
#     """This demo illustrates a combination of plotting and animation with
# Streamlit. We're generating a bunch of random numbers in a loop for around
# 5 seconds. Enjoy!"""
# )
tokenData = asyncio.run(fetchTokenData())
#tokenData = await fetchTokenData()
print(type(tokenData))
tokentransfer_df = tokenData[0]
tokenbalance_df = tokenData[1]
tab1, tab2 = st.tabs(["Token Transfers", "Token Balance"])
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

with tab1:
   st.header("Token Transfers")
   # Download CSV button
   csv = convert_df(tokentransfer_df)
   st.download_button(
    "Download Data (.csv)",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )
   for i in range(0, 50):
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)

with tab2:
   st.header("Token Balance")
   # Download CSV button
   csv = convert_df(tokenbalance_df)
   st.download_button(
    "Download Data (.csv)",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv2'
    )
   st.dataframe(tokenbalance_df)
   for i in range(51, 101):
        status_text.text("%i%% Complete" % i)
        progress_bar.progress(i)
        time.sleep(0.05)

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")