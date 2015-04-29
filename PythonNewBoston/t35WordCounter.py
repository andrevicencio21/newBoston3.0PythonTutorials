import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    h2 = soup.find_all('h2').find_parent()
  

    
    

start(r'http://www.dota2.com/684')