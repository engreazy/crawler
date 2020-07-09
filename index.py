def get_webpage():
  page_name = input('enter page name >>> ') #prompt user for the name of the file to open
  page = open(page_name) #open the file entered by user
  savePage = open('save.txt','w') # open the file to save the results for all url
  print(f"reading file {page_name} content")
  print(f"{'.' * 30 }")
  # print(f"type of page content is ")
  # print(type(page.read()))
  print_all_links(page.read(),savePage)
  savePage.close()
  page.close()

def find_page_link(page_content):
  link_tag = '<a href=' # anchor tag
  #print("find_page_link called") uncomment for debugging
  start_link = page_content.find(link_tag) # find the first position of the anchor tag
  if (start_link + 1):
    #print(page_content) # print the page content
    start_quote = page_content.find('"',start_link) # find the first quote position between the anchor tag
    end_quote = page_content.find('"',start_quote + 1) # find the last quote position between the anchor tag
    url = page_content[start_quote + 1:end_quote] #retrieve the url between the quotes of the anchor tag
    # print("the url is => ")
    return url, end_quote
  else:
    # print("No link tag found!")
    return None, 0


def print_all_links(page_content,save_page_content):
  #print("print_all_links called") uncomment for debugging
  all_links = []
  while True:
    url, end_pos = find_page_link(page_content)
    if url:
      # print(url)
      all_links += [url]
      page_content = page_content[end_pos:]
      save_page_content.write(url)
      save_page_content.write("\n")
    else:
      print(all_links)
      break

def get_all_page_links(page_content):
  all_links = []
  links = []
  while True:
    url, end_pos = find_page_link(page_content)
    if url:
      all_links += [url]
      links.append(url)
    else:
      break
  return links, all_links

get_webpage()
