#! python3
# Opens several google search results.

import requests, sys, webbrowser, bs4

print('Googling...') #Display text while downloading the Google page
res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "lxml")

# Open a browser tab for each results
linkElems = soup.select('.r a')
numOpens = min(5,len(linkElems))
for i in range(numOpens):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))
