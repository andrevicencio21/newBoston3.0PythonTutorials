import random
import urllib.request

def imageDownloader(url):
    name = random.randrange(1, 1000)
    fullName = str(name) + ".png"
    urllib.request.urlretrieve(url, fullName) #2nd argument will be fileName

imageDownloader("https://imagizer.imageshack.us/v2/801x451q90/905/CV6dLA.png")
    
