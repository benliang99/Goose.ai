# Using existing Subgraph https://thegraph.com/hosted-service/subgraph/gjeanmart/gnosis-safe-goerli
# https://towardsdatascience.com/connecting-to-a-graphql-api-using-python-246dda927840

import requests
import json
import pandas as pd
from datetime import datetime

# Enter this URL into your browser and click "Explorer" to filter by data types
# @andrew you can use this to generate queries to copy paste into these function 
# templates. Example: you can use "where: {variable}"
API_URL = 'https://api.thegraph.com/subgraphs/name/gjeanmart/gnosis-safe-goerli'

def prepareJSON(query):
    r = requests.post(API_URL, json={'query': query})
    return json.loads(r.text)

# Query that retrieves all transactions with a Gnosis Safe wallet and 
# sorts by descending order.
def txDescending():
    query = """
    query {
        transactions(where: {value_not: null}, orderBy: value, orderDirection: desc) {
            block
            data
            destination
            estimatedBaseGas
            estimatedSafeTxGas
            gasPrice
            gasToken
            id
            hash
            nonce
            operation
            payment
            refundReceiver
            signatures
            stamp
            status
            txhash
            value
        }
    }
    """
    json_data = prepareJSON(query)
    transactions_data = json_data['data']['transactions']
    transactions_df = pd.DataFrame(transactions_data)
    transactions_df['stamp'] = pd.to_datetime(pd.to_numeric(transactions_df['stamp']), unit='s')
    return transactions_df

# Query that retrieves about any specific transaction
def txInfo(address):
    query = f"""
    query {{
        transaction(id: "{address}") {{
            id
            nonce
            operation
            payment
            refundReceiver
            signatures
            stamp
            status
            txhash
            value
            hash
            gasToken
            gasPrice
            estimatedBaseGas
            estimatedSafeTxGas
            destination
            data
            block
        }}
    }}
    """
    json_data = prepareJSON(query)
    tx_data = json_data['data']['transaction']
    tx_df = pd.DataFrame(tx_data, index=[0])
    tx_df['stamp'] = pd.to_datetime(pd.to_numeric(tx_df['stamp']), unit='s')
    return tx_df

# Query that retrieves info about any specific wallet
def walletInfo(address):
    query = f"""
    query {{
        wallet(id: "{address}") {{
            creator
            currentNonce
            factory
            hash
            id
            mastercopy
            network
            owners
            stamp
            threshold
        }}
    }}
    """
    json_data = prepareJSON(query)
    wallet_data = json_data['data']['wallet']
    wallet_df = pd.DataFrame(wallet_data)
    wallet_df['stamp'] = pd.to_datetime(pd.to_numeric(wallet_df['stamp']), unit='s')
    return wallet_df

# Returns the first wallets from the query, which is the same order every time, but 
# the timestamps seem sort of random? Might be how the initial data upload worked
def firstWalletsFromQuery(num):
    query = """
    query {
        wallets(first: %d) {
            id
            creator
            network
            stamp
        }
    }
    """ % num
    json_data = prepareJSON(query)
    wallets_data = json_data['data']['wallets']
    wallets_df = pd.DataFrame(wallets_data)
    wallets_df['stamp'] = pd.to_datetime(pd.to_numeric(wallets_df['stamp']), unit='s')
    return wallets_df

def firstTxsFromQuery(num):
    query = """
    query {
        transactions(first: %d) {
            id
            stamp
            block
            hash
        }
    }""" % num
    json_data = prepareJSON(query)
    transactions_data = json_data['data']['transactions']
    transactions_df = pd.DataFrame(transactions_data)
    transactions_df['stamp'] = pd.to_datetime(pd.to_numeric(transactions_df['stamp']), unit='s')
    return transactions_df

def main():
    #print(walletInfo("0x00051af42c82bfa5c10e7ea75b71df8b58b10b44"))
    #print(txInfo("0x0000ca5f43b6eaf5a05abe152f878f252df8d7178ed2ee617e2d58d59ffe49a5"))
    print(txDescending())
    return

main()