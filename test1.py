import sys
import requests		# Requests required to obtain webpage
import bs4		# BS4 required to parse webpage


argv = sys.argv
final_string = ''
keyword = ''
# https://www.google.com/search?q=imagenet%20how%20many%20images
for i in range(1,len(argv)):
  final_string+= argv[i] + '%20'
  keyword += argv[i] + ' '
my_url = "https://www.google.com/search?q="+final_string
# print("Your final url : \n"+url)

#Setting Query Parameters for Search 
params = [('q',keyword)]

#Google Search URL
url = "https://google.co.in/search"

# Gets response from the server for the search query
response = requests.get(url=url, params=params)

# Response text from server is parsed using bs4
soup = bs4.BeautifulSoup(response.text,'lxml')

# Titles of results are found (Assumed that Google put h3 only on result titles)
titles = soup.find_all("h3")
mydivs = soup.find_all("div", {"class": "BNeawe s3v9rd AP7Wnd"})
# <div class="IZ6rdc">Mahatma Gandhi</div>
# div class="BNeawe s3v9rd AP7Wnd"

# print(mydivs)
print(len(mydivs))
# print(soup)
# 	print( str(x) + ". " + title.get_text() )
