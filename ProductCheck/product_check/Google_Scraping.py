from bs4 import element
from requests import NullHandler
from serpapi import GoogleSearch

class FilterLogic:
  def __init__(self):
      self.results = {}

  def searchQueryAmazon(self):
    params = {
    "engine": "google",
    "q": "mattress amazon.com",
    "api_key": "4ac8179c2b83da5e87019484de602805a72a7d1581b8f004efe4d9939e99e857"
  }
    search = GoogleSearch(params)
    self.results = search.get_dict()
    return self.results

  def searchQueryWalmart(self):
    params = {
    "engine": "walmart",
    "query": "mattress",
    "api_key": "4ac8179c2b83da5e87019484de602805a72a7d1581b8f004efe4d9939e99e857"
  }
    search = GoogleSearch(params)
    self.results = search.get_dict()
    return self.results

  def searchQueryGoogleCostco(self):
    params = {
    "engine": "Google",
    "q": "mattress Costco.com",
    "api_key": "4ac8179c2b83da5e87019484de602805a72a7d1581b8f004efe4d9939e99e857"
  }
    search = GoogleSearch(params)
    self.results = search.get_dict()
    return self.results

  def searchQueryGoogleTarget(self):
    params = {
    "engine": "Google",
    "q": "mattress Target.com",
    "api_key": "4ac8179c2b83da5e87019484de602805a72a7d1581b8f004efe4d9939e99e857"
  }
    search = GoogleSearch(params)
    self.results = search.get_dict()
    return self.results
  
  def GoogleAmazon(self,results):
    links = []
    for i in range(0,len(results)):
      if "Amazon.com" in results['shopping_results'][i]['source']:
        links.append(results['shopping_results'][i]['link'])

    print(links)

  def GoogleTarget(self,results):
    #uses shopping lists
    links = []
    for i in range(0,len(results)):
      if results['shopping_results'][i]['source'] == "Target":
        links.append(results['shopping_results'][i]['link'])

    return links
  
  def GoogleCotsco(self,results):
    #uses organic results
    links = []
    for i in range(0,len(results)):
      try:
        if "www.costco.com" in results['organic_results'][i]['link'] and results['organic_results'][i]['sitelinks']:
          for k in  results['organic_results'][i]['sitelinks']['expanded']:
            links.append(k['link'])
      except:
        print('error')
    return links
      

  #walmart results 
  def filterByRatings(self, results):
    links = []
    for i in range(0,len(results)):
      links.append([results['organic_results'][i]['product_page_url']])
    return links
    
    
    # sorted_list = {}
    # sorted_list = sorted(link.items(), key=lambda x: x[1])    
    # res1 = {}
    # for i in range(0,len(sorted_list)):
    #   for j in range(0,len(results)):
    #     if results['organic_results'][j]['product_page_url'] == sorted_list[i][0]:
    #       x = {}
    #       x['rating'] = results['organic_results'][j]['rating']
    #       y = {}
    #       y['price'] = results['organic_results'][j]['price_per_unit']['amount']
    #       l = []
    #       l.append(x)
    #       l.append(y)
    #   res1[sorted_list[i][0]] = l

    #   print(res1)
    







