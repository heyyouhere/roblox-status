import requests
import urllib3
import json
#Using https://core.telegram.org/bots/api as reference

class TelegramBot():
    def __init__(self, token):
        self.url = 'https://api.telegram.org/bot'+ str(token) 
        self.offset = None
        self.getUpdates()

    def sendMessage(self, chat_id, text, parse_mode = 'MarkdownV2', reply_to_message_id = 0, allow_sending_without_reply = 'True'):
        args = 'chat_id=' + str(chat_id) + '&text=' + str(text) + '&reply_to_message_id=' + str(reply_to_message_id) + '&parse_mode=' + str(parse_mode) + '&allow_sending_without_reply=' + str(allow_sending_without_reply)
        return requests.post(self.url + '/sendMessage?' + args)
        
    
    def getUpdates(self):
        if self.offset != None:
            updates = requests.get(self.url + '/getUpdates?timeout=2&offset=' + str(self.offset) ).content
            parsed_updates = json.loads(updates)
            # print(parsed_updates)
            if parsed_updates.get('result'):
                self.offset = int(parsed_updates['result'][-1]['update_id']) + 1
            return parsed_updates 
        else:
            updates = requests.get(self.url + '/getUpdates?timeout=2&offset=0').content
            parsed_updates = json.loads(updates)
            # print(parsed_updates)
            if parsed_updates.get('result'):
                self.offset = int(parsed_updates['result'][-1]['update_id'])
                self.getUpdates()
            
    def getMe(self):
        return requests.get(self.url + '/getMe')
    
