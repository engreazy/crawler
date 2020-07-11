#Finish crawl web
import requests

def getPage(url):
  request = requests.get(url);
  return request.text

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    #print(page)
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            #print(f"url is => {url}")
            links.append(url)
            page = page[endpos:]
            #print("page is now =>")
            #print(page)
        else:
            break
    return links

def crawl_web(seed):
    print("crawl web called")
    tocrawl = [seed] #seed page to start web crawler
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
          union(tocrawl,get_all_links(getPage(page)))
          print("value of tocrawl => ", tocrawl)
          print("value of crawled =>", crawled)
          crawled.append(page)
    print("*" * 50)
    print("tocrawl final is =>")
    print(tocrawl)
    print("crawled final is =>")
    print(crawled)
    print(f"total links of crawled {str(len(crawled))}")
    return crawled

#crawl_web("http://xkcd.com/353")
crawl_web("https://udacity.github.io/cs101x/index.html")


