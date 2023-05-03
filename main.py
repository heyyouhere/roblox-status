import robloxstatus
from mytelegrambot import TelegramBot
from time import sleep

token = open('token.txt', 'r').read()
bot = TelegramBot(str(token).strip())
group_id = '-1001639400973'


last_status = ''
while True:
    status = robloxstatus.getStatus() 
    if status != 'All Systems Operational':
        bot.sendMessage(group_id, text = f'Roblox might be down/! New status: \n{status}')
        print(f'Roblox might be down/! New status: \n{status}')
    else:
        if last_status != 'All Systems Operational' and last_status != '':
            bot.sendMessage(group_id, text = f'Roblox is back to operational\!')
            print(f'Roblox is back to operational/!')
    last_status = status
    sleep(60 * 10)



