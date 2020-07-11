import requests,bs4

def getWebPageContent(url):
  request = requests.get(url)
  pageContent = request.text
  return pageContent

def findWebPageLink(pageContent):
    soup = bs4.BeautifulSoup(pageContent,'lxml')
    #print('page Document => ',soup.prettify())
    #find all links
    all_links = soup.find_all('a')
    # print("find all links => ",all_links)
    # print("total links are => ", len(all_links))
    allLinks = []
    for link in all_links:
      allLinks.append(link.get('href'))
    return allLinks

def union(first,second):
    for x in second:
        if x not in first:
            first.append(x)

a = [1,2,3]
b = [2,4,5,6]
#union(a,b)
#print(a)
#>>> [1,2,3,4,5,6]
#print(b)
#>>> [2,4,6]

def webCrawler(seedPageUrl):
  toCrawl = [seedPageUrl]
  crawled = []
  while toCrawl:
    webPageUrl = toCrawl.pop()
    if webPageUrl not in crawled:
      union(toCrawl,findWebPageLink(getWebPageContent(webPageUrl)))
      # print("value of toCrawl =>", toCrawl)
      # print("value of crawled =>", crawled)
    crawled.append(webPageUrl)
  print("*" * 50)
  print("toCrawl final is => ", toCrawl)
  print("crawled final is => ", crawled)
  print("*" * 50)
  print(f"total links crawled => {str(len(crawled))}")
  return crawled


webCrawler("https://udacity.github.io/cs101x/index.html")