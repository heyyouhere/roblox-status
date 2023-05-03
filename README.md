# Roblox Status Bot
Simple bot, that parses [this](https://status.roblox.com) website, and watches on Roblox Status changes. It'll notify team, in Telegram group chat, if something is up (or down).

## Get your token
Go to [Telegram](https://telegram.org), and find [@BotFather](https://t.me/BotFather). He'll guide you through the process.

## Get your group chat id 
1. Login to Telegram WebZ.
2. Open the chat you want to get its ID.
3. Your browser's address should look like https://web.telegram.org/z/#-1527776602.
4. Remove the protocol, domain and path keeping the anchor so your result looks like #-1527776602.
5. Replace "#-" with "-100" so it looks like -1001527776602.
6. You can now use your final result which should look like -1001527776602.

More ways to get it and source is [here](https://stackoverflow.com/a/72649378).
ty stackoverflow! 

## Usage
```console
echo <your_token_here> >> token.txt
python3 main.py
```

## mytelegrambot.py
I'm testing my own super simple (yet another) telegram bot api library. Feedback is welcomed. 
