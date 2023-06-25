# Voiceflow x Telegram

TLDR, run:

npm install && node app.js

## Prerequisites

Here you have the technologies used in this project
1. Telegram account
2. Voiceflow Account

## Voiceflow authentication
For authentication, we will need to get our VF Project API key. 

To access the Project API key for a specific project:

1. Open the project you want to connect with
2. Select on the Integrations tab (shortcut: 3)
3. Copy the Dialog API Key.

![project api](https://user-images.githubusercontent.com/68556615/161978440-7c6a2605-5721-489e-ae1b-a9fd68db84e7.png)


Add the credentials into your `.env` file
```
VF_API_KEY= "VF.xxxxx"
```

## Create Telegram Bot

First, We should create our own bot with BotFather.

If you open a chat with a BotFather, click on the “Start” button.

![telegram](https://user-images.githubusercontent.com/68556615/161981056-134b351a-d46b-444a-82fd-ddd8578ed2ef.png)

Create a new bot by typing the `/newbot` command. Next, you should enter any name for the bot. In this example, we named it Voiceflow Bot.

Add your Telegram token to your `.env` file

```
BOT_TOKEN= "xxxxx"
```

## Setting up the Project

Install and run the project:

1. Clone this repo:
```bash
git clone https://github.com/zslamkov/voiceflow_telegram.git
```

2. Install dependencies:
```bash
npm install
```

## Telegraf setup 
We can setup the bot using the following code:

```js
const {Telegraf} = require('telegraf') // import telegram lib
const bot = new Telegraf(process.env.BOT_TOKEN)
bot.start((ctx) => ctx.reply('Welcome')) 
bot.hears('hi', (ctx) => ctx.reply('Hey there'))
bot.launch() // start

process.once('SIGINT', () => bot.stop('SIGINT'))
process.once('SIGTERM', () => bot.stop('SIGTERM'))
```

Next, we will update the `start` and `hears` methods to interact with Voiceflow's Dialog Manager and return the relevant next message in the conversation. 

```js 
bot.start(async (ctx) => {
    let USER_ID = ctx.message.chat.id;
    console.log(USER_ID);
    await interact(ctx, ctx.message.chat.id, {type: "launch"});
});

const ANY_WORD_REGEX = new RegExp(/(.+)/i);
bot.hears(ANY_WORD_REGEX, async (ctx) => {
    await interact(ctx, ctx.message.chat.id, {
        type: "text",
        payload: ctx.message.text
    });
});
```

## Voiceflow `/interact` request
Finally, we will pass the request into the below function which sends a `post` request to Voiceflow's Dialog Manager API to retrieve the next step in the conversation. The expected response will be an array of _n_ trace types which we will iterate through and map each trace type to the desired output in Telegram.

```js
async function interact(ctx, chatID, request) {

    const response = await axios({
        method: "POST",
        url: `https://general-runtime.voiceflow.com/state/user/${chatID}/interact`,
        headers: {
            Authorization: process.env.VOICEFLOW_API_KEY
        },
        data: {
            request
        }
    });
    for (const trace of response.data) {
        switch (trace.type) {
            case "text":
            case "speak":
                {
                    await ctx.reply(trace.payload.message);
                    break;
                }
            case "visual":
                {
                    await ctx.replyWithPhoto(trace.payload.image);
                    break;
                }
            case "end":
                {
                    await ctx.reply("Conversation is over")
                    break;
                }
        }
    }
};
```

## Running the Telegram Bot

![telegram_gif](https://user-images.githubusercontent.com/68556615/161981493-363a3c18-de1d-4ba7-b458-321d077ec7e9.gif)
