import requests
import json
import pandas as pd
from datetime import datetime

# The UMA subgraph indexes data from UMA contracts over time. It organizes data
# about tokenholders, contracts, DVM requests, voting, and more. The subgraph
# updates for each UMA contract interaction. 

# https://thegraph.com/explorer/subgraph?id=41LCrgtCNBQyDiVVyZEuPxbvkBH9BxxLU3nEZst77V8o&view=Overview
API_KEY = 'dc600989321fa0012e06d1a111a29d60'
API_URL = 'https://gateway.thegraph.com/api/'+API_KEY+'/subgraphs/id/41LCrgtCNBQyDiVVyZEuPxbvkBH9BxxLU3nEZst77V8o'

# Retrieve data about: User, PriceIdentifier, PriceRequest, PriceRequestRound,
# VoterGroup, CommittedVote, RevealedVote, RewardsClaimed

def prepareJSON(query):
    r = requests.post(API_URL, json={'query': query})
    return json.loads(r.text)

def voterGroups(num):
    query = """
    {
        voterGroups(first: %d){
            id
            price
            round
            votes{
                id
            }
            totalVoteAmount
            totalVoteAmount
            votersAmount
            won
        }
    }
    """ % num
    json_data = prepareJSON(query)
    voterGroups_data = json_data['data']['voterGroups']
    voterGroups_df = pd.DataFrame(voterGroups_data)
    return voterGroups_df

# Users, descending by votes correctly voted for
def userDescendingByNumCorrectVotes():
    query = """
    {
        users(where: {countRetrievals_not: null}, orderBy: countRetrievals, orderDirection: desc) {
            id
            address
            countReveals
            countRetrievals
            votesCommited{
                id
            }
        }   
    }"""
    json_data = prepareJSON(query)
    users_data = json_data['data']['users']
    users_df = pd.DataFrame(users_data)
    return users_df

def userDescendingByNumVotes():
    query = """
    {
        users(where: {countReveals_not: null}, orderBy: countReveals, orderDirection: desc) {
            id
            address
            countReveals
            countRetrievals
            votesCommited{
                id
            }
        }   
    }"""
    json_data = prepareJSON(query)
    users_data = json_data['data']['users']
    users_df = pd.DataFrame(users_data)
    return users_df

# Query that retrieves info about any specific user
def user(id):
    query = f"""
    query {{
        user(id: "{id}") {{
            id
            address
            countReveals
            countRetrievals
            votesCommited
        }}
    }}
    """
    json_data = prepareJSON(query)
    user_data = json_data['data']['user']
    user_df = pd.DataFrame(user_data, index=[0])
    return user_df

def priceRequestsAscending():
    query = """
    {
        priceRequests(where: {resolutionTimestamp_not: null}, orderBy: resolutionTimestamp, orderDirection: asc){
            id
            isResolved
            price
            latestRound
            time
            identifier
            ancillaryData
            resolutionTransaction
            resolutionTimestamp
            resolutionBlock
            rounds{
                id
            }
            committedVotes{
                id
            }
            revealedVotes{
                id
            }
            rewardsClaimed{
                id
            }
        }
    }
    """
    json_data = prepareJSON(query)
    priceRequests_data = json_data['data']['priceRequests']
    priceRequests_df = pd.DataFrame(priceRequests_data)
    return priceRequests_df

def priceRequestsDescending():
    query = """
    {
        priceRequests(where: {resolutionTimestamp_not: null}, orderBy: resolutionTimestamp, orderDirection: desc){
            id
            isResolved
            price
            latestRound
            time
            identifier
            ancillaryData
            resolutionTransaction
            resolutionTimestamp
            resolutionBlock
            rounds{
                id
            }
            committedVotes{
                id
            }
            revealedVotes{
                id
            }
            rewardsClaimed{
                id
            }
        }
    }
    """
    json_data = prepareJSON(query)
    priceRequests_data = json_data['data']['priceRequests']
    priceRequests_df = pd.DataFrame(priceRequests_data)
    return priceRequests_df

def firstPriceRequests(num):
    query = """
    {
        priceRequests(first: %d){
            id
            isResolved
            price
            latestRound
            time
            identifier
            ancillaryData
            resolutionTransaction
            resolutionTimeStamp
            resolutionBlock
            rounds{
                id
            }
            committedVotes{
                id
            }
            revealedVotes{
                id
            }
            rewardsClaimed{
                id
            }

        }
    }
    """ % num
    json_data = prepareJSON(query)
    priceRequests_data = json_data['data']['priceRequests']
    priceRequests_df = pd.DataFrame(priceRequests_data)
    return priceRequests_df

def firstPriceIdentifiers(num):
    query = """
    {
        priceIdentifiers(first: %d) {
            id
            isSupported
            priceRequests {
                id
            }
        }
    }
    """ % num
    json_data = prepareJSON(query)
    priceIdentifiers_data = json_data['data']['priceIdentifiers']
    priceIdentifiers_df = pd.DataFrame(priceIdentifiers_data)
    return priceIdentifiers_df

def firstUsers(num):
    query = """
    {
        users(first: %d) {
            id
            address
            countReveals
            countRetrievals
        }   
    }""" % num
    json_data = prepareJSON(query)
    users_data = json_data['data']['users']
    users_df = pd.DataFrame(users_data)
    return users_df

def main():
    #print(walletInfo("0x00051af42c82bfa5c10e7ea75b71df8b58b10b44"))
    #print(txInfo("0x0000ca5f43b6ea f5a05abe152f878f252df8d7178ed2ee617e2d58d59ffe49a5"))
    #print(firstPriceRequests(5))
    #print(priceRequestsDescending())
    #print(priceRequestsAscending())
    #print(firstUsers(5))
    #print(user("0x000000aaee6a496aaf7b7452518781786313400f"))
    #print(userDescendingByNumVotes())
    #print(userDescendingByNumCorrectVotes())
    print(voterGroups(5))
    return

main()
