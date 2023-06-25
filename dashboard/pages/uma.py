import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
import plotly_express as px
from utils.uma_mainnet_voting_data_retrieval import *

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# UMA")
st.sidebar.header("UMA")
st.write(
    """Data from UMA Protocol x The Graph"""
)

# Load gnosis data from utils

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Voter Groups", "User Correct Votes", "User Num Votes",
                                          "Specific User", "Price Requests",
                                          "Price Identifiers", "Users"])

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

with tab1:
   st.header("Voter Groups")
   # Download CSV button
   st.write(
    """Voter Group Data"""
    )
   number = st.number_input('Number of voter groups to display', min_value=1, step=1)
   voterGroups_df = voterGroups(number)
   csv = convert_df(voterGroups_df)
   st.download_button(
    "Download Data (.csv)",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )
   if(number > 0):
    st.dataframe(voterGroups_df)
   for i in range(0, 9):
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)

with tab2:
   st.header("User Correct Votes")
   # Download CSV button
   st.write(
    """Number of Correct Votes per User"""
    )
   userDescendingByNumCorrectVotes_df = userDescendingByNumCorrectVotes()
   csv = convert_df(userDescendingByNumCorrectVotes_df)
   st.download_button(
    "Download Data (.csv)",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv2'
    )
   st.dataframe(userDescendingByNumCorrectVotes_df)
   for i in range(10, 24):
        status_text.text("%i%% Complete" % i)
        progress_bar.progress(i)
        time.sleep(0.05)
   

with tab3:
   st.header("User Num Votes")
   # Download CSV button
   st.write(
    """Number of Votes per User"""
    )
   userDescendingByNumVotes_df = userDescendingByNumVotes()
   csv = convert_df(userDescendingByNumVotes_df)
   st.download_button(
    "Download Data (.csv)",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv3'
    )
   st.dataframe(userDescendingByNumVotes_df)
   for i in range(25, 39):
        status_text.text("%i%% Complete" % i)
        progress_bar.progress(i)
        time.sleep(0.05)


with tab4:
   st.header("Specific User")
   # Download CSV button
   st.write(
    """Data Attributed to a Wallet Address"""
    )
   userID = st.text_input('User ID', placeholder="Enter ID here")
   specificUser_df = user(userID)
   csv = convert_df(specificUser_df)
   st.download_button(
    "Download Data (.csv)",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv4'
    )
   st.dataframe(specificUser_df)
   for i in range(40, 54):
        status_text.text("%i%% Complete" % i)
        progress_bar.progress(i)
        time.sleep(0.05)

with tab5:
   st.header("Price Requests")
   # Download CSV button
   priceRequestsAscending_df = priceRequestsAscending()
   csv = convert_df(priceRequestsAscending_df)
   st.download_button(
    "Download Data (.csv)",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv5'
    )
   st.dataframe(priceRequestsAscending_df)
   for i in range(55, 69):
        status_text.text("%i%% Complete" % i)
        progress_bar.progress(i)
        time.sleep(0.05)

with tab6:
   st.header("Price Identifiers")
   # Download CSV button
   number = st.number_input('Number to display', min_value=1, step=1)
   firstPriceIdentifiers_df = firstPriceIdentifiers(number)
   csv = convert_df(firstPriceIdentifiers_df)
   st.download_button(
    "Download Data (.csv)",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv6'
    )
   if(number > 0):
    st.dataframe(firstPriceIdentifiers_df)
   for i in range(70, 84):
        status_text.text("%i%% Complete" % i)
        progress_bar.progress(i)
        time.sleep(0.05)

with tab7:
   st.header("Users")
   # Download CSV button
   number = st.number_input('Number of users to display', min_value=1, step=1)
   users_df = firstUsers(number)
   csv = convert_df(users_df)
   st.download_button(
    "Download Data (.csv)",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv7'
    )
   if(number > 0):
    st.dataframe(users_df)
    
   for i in range(85, 101):
        status_text.text("%i%% Complete" % i)
        progress_bar.progress(i)
        time.sleep(0.05)
   progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")