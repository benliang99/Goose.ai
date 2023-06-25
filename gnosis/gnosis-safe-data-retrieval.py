# Using existing Subgraph https://thegraph.com/hosted-service/subgraph/gjeanmart/gnosis-safe-goerli
# https://towardsdatascience.com/connecting-to-a-graphql-api-using-python-246dda927840

import requests
import json
import pandas as pd
from datetime import datetime

# Enter this URL into your browser and click "Explorer" to filter by data types
API_URL = 'https://api.thegraph.com/subgraphs/name/gjeanmart/gnosis-safe-goerli'

# Example query that retrieves 
query = """query {
    wallets(first: 5) {
    id
    creator
    network
    stamp
  }
  transactions(first: 5) {
    id
    stamp
    block
    hash
  }
}"""

url = 'https://api.thegraph.com/subgraphs/name/gjeanmart/gnosis-safe-goerli'
r = requests.post(url, json={'query': query})
#print(r.status_code)
#print(r.text)

json_data = json.loads(r.text)
wallets_data = json_data['data']['wallets']
transactions_data = json_data['data']['transactions']

wallets_df = pd.DataFrame(wallets_data)
transactions_df = pd.DataFrame(transactions_data)

# Convert 'stamp' column to datetime in both dataframes
wallets_df['stamp'] = pd.to_datetime(pd.to_numeric(wallets_df['stamp']), unit='s')
transactions_df['stamp'] = pd.to_datetime(pd.to_numeric(transactions_df['stamp']), unit='s')

print(wallets_df)
print(transactions_df)