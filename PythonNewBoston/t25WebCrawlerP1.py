import requests
from bs4 import BeautifulSoup







def matchSpider(maxPages):
    page = 1
    while page <= maxPages:
        url = r'http://www.gosugamers.net/dota2/gosubet?u-page=1'
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for link in soup.find_all('a', {'class':'match hover-background'}):
            href = r'http://www.gosugamers.net' + link.get('href')
            getItemData(href)
        page += 1
        
def getItemData(itemUrl):
        sourceCode = requests.get(itemUrl)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for div1 in soup.find_all('div', {'class':'opponent opponent1'}):
            for teams in div1.find_all('a'):
                teamName = teams.string
                print(teamName, end=" vs. ")
        for div2 in soup.find_all('div', {'class':'opponent opponent2'}):
            for teams in div2.find_all('a'):
                teamName = teams.string
                print(teamName, end='')
        for timers in soup.find_all('span',{'class': 'countdown'}):
            print(timers.text)
            #print("    TimeRemaning: " + str(timeRemaning))

matchSpider(1)