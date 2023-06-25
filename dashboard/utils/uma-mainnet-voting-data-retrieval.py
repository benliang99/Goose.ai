import requests
import json
import pandas as pd
from datetime import datetime

# https://thegraph.com/explorer/subgraph?id=41LCrgtCNBQyDiVVyZEuPxbvkBH9BxxLU3nEZst77V8o&view=Overview
API_KEY = 'dc600989321fa0012e06d1a111a29d60'
API_URL = 'https://gateway.thegraph.com/api/'+API_KEY+'/subgraphs/id/41LCrgtCNBQyDiVVyZEuPxbvkBH9BxxLU3nEZst77V8o'

def prepareJSON(query):
    r = requests.post(API_URL, json={'query': query})
    return json.loads(r.text)

def firstFiveUsers(num):
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
    print(firstFiveUsers(5))
    return

main()
