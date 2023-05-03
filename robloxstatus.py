import requests
from bs4 import BeautifulSoup


def getStatus():
    html = requests.get('https://status.roblox.com/').content
    soup = BeautifulSoup(html, features = 'html.parser')
    status = soup.find('strong', {'id' : 'statusbar_text'}).text
    return status

if __name__ == '__main__':
    status = getStatus()
    print(status)
