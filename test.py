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


#Title Text Block
# print("GOOGLE SCRAPING USING PY3 AND BS4 \n")

#Accepts Search Keywords from the User
# keyword = input("ENTER SEARCH KEYWORDS: ")

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
mydivs = soup.find_all("div", {"class": "IZ6rdc"})
# <div class="IZ6rdc">Mahatma Gandhi</div>
#Result is Displayed

# print("\nDISPLAYING FIRST PAGE RESULT TITLES FOR " + keyword + "\n")
print(mydivs)
# x = 0; # counter variable
# for title in titles: #loop to display titles
# 	x=x+1 # counter updated
# 	print( str(x) + ". " + title.get_text() )
