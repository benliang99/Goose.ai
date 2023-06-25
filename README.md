# 🍁 Goose.ai

### Goose.ai brings everything blockchain has to offer to mobile, Discord, Slack, and Telegram!

## 💡 Inspiration 

**The barrier of entry to Web3 is** ***HIGH.*** On September 26, 2022, The Ontario Securities Commission published a Crypto Asset Survey Report and found that amongst Canadians:

* the average crypto asset knowledge score was 37%
* few felt particularly familiar with crypto
* most lacked a working knowledge of the practical, legal, or regulatory dimensions of crypto assets

And this is just crypto, arguably the most publicly recognizable part of the Web3 umbrella! So how do we lower the barrier of entry to crypto, blockchain, and Web3 services? With **Goose.ai**! 🤖

## ❓ What it does

Goose.ai is a multipurpose, platform-agnostic tool that uses an LLM-driven chatbot to increase accessibility to Web3 services and blockchain data visualization tools. Ask questions about specific Web3 technologies, get insights on live data feeds, and **make blockchain state changes** all through chat.

Technologies: WorldCoin login, Gnosis Safe, Polygon, IPFS, Web3.Storage, The Graph subgraphs, AirStack APIs, UMA, Quicknode, NounsDAO, Highlight, ApeCoin 

## 🚧 How we built it 

1. We are leveraging **WorldCoin's World ID** to provide secure authentication login for our POAP minting webpage! (We don't want people or bots spamming our POAP minting and taking it away from genuine users)
   
2. We leveraged **Quicknode's NFT API** to allow all 650 hackers to mint their own ETHWaterloo 2023 POAP via chat using Goose.ai on the Polygon mainnet and testnet!
     - Mint your own ETHWaterloo 2023 POAP via text using Goose.ai **(Quicknode NFT API, Polygon)**.
     - Choose from:
       - a **Noun** unique to your wallet address **(Nouns-API)**.
       - a classic Mr. Goose GIF if you want the original image.
       - an AI generated Mr. Goose image with any traits you want OpenAI's Text-To-Image model (Eden AI API).
      
3. Backup your NFTs on any chain through chat **(IPFS and Web3.Storage)**

4. Interchain functionality via chat
   - Use Warp routes to transact across multiple chains! **(HyperLane)**

5. Data visualization dashboard (Streamlit app)
     - Monitor your Gnosis Safe wallet's transactions, ownership status, creation date and more! **(The Graph, Gnosis Safe)**
        - Find trends using our interactive plotting feature using data from the Gnosis Safe subgraph
        - Enter your Gnosis Safe wallet address or transaction address to get information instantly
        - Download the data you selected as a .csv
     - Monitor UMA Mainnet Voting Entities **(The Graph, UMA)**
        -  Retrieve data about: User, PriceIdentifier, PriceRequest, PriceRequestRound, VoterGroup, CommittedVote, RevealedVote, RewardsClaimed
     - Retrieve and visualize marketplace data **(Airstack)**
     - Monitor ApeCoin activity **(Snapshot/GraphQL, ApeCoin DAO)**

Check out our [ETHGlobal page](https://ethglobal.com/showcase/goose-ai-3tgh9)! Goose.ai is an [ETHGlobal Waterloo](https://ethglobal.com/events/waterloo2023) project.

