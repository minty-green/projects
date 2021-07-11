import requests
import re
from bs4 import BeautifulSoup

input1 = input("Input your carousell search here! : ")
input2 = "https://www.carousell.sg/search/" + input1 + "?addRecent=true&canChangeKeyword=true&includeSuggestions=true" \
                                                       "&sort_by%22%22=time_created%2Cdescending "

result = requests.get(input2)

src = result.content
soup = BeautifulSoup(src, "lxml")
links = soup.find_all("a")


item = re.findall('/p/..............................................................................................+[0-9]', str(links))
print(item)
