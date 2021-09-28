""" 
Scraping multiple ecommerce sites to obtain poduct links using serpAPI

"""

from bs4 import element
from requests import NullHandler
from serpapi import GoogleSearch

class FilterLogic:
  def __init__(self):
      self.results = {}
      self.Amazon = "Amazon.com"
      self.Target = "Target"
      self.Costco = "Costco"
      self.Walmart = "walmart"

  def searchQueryAmazon(self,key):
    params = {
      "tbm": "shop",
      "hl": "en",
      "gl": "us",
      "engine": "google",
      "q": key+" "+"Amazon.com",
      "api_key": "4ac8179c2b83da5e87019484de602805a72a7d1581b8f004efe4d9939e99e857"
  }
    search = GoogleSearch(params)
    self.results = search.get_dict()
    return self.results

  def searchQueryWalmart(self,key):
    params = {
    "tbm": "shop",
    "hl": "en",
    "gl": "us",
    "engine": "google",
    "q": key+" "+"walmart.com",
    "api_key": "4ac8179c2b83da5e87019484de602805a72a7d1581b8f004efe4d9939e99e857"
}
    search = GoogleSearch(params)
    self.results = search.get_dict()
    return self.results

  def searchQueryGoogleCostco(self,key):
    params = {
      "tbm": "shop",
      "hl": "en",
      "gl": "us",
      "engine": "google",
      "q": key+" "+"Costco.com",
      "api_key": "4ac8179c2b83da5e87019484de602805a72a7d1581b8f004efe4d9939e99e857"
  }
    search = GoogleSearch(params)
    self.results = search.get_dict()
    return self.results

  def searchQueryGoogleTarget(self,key):
    params = {
      "tbm": "shop",
      "hl": "en",
      "gl": "us",
      "engine": "google",
      "q": key+" "+"Target.com",
      "api_key": "4ac8179c2b83da5e87019484de602805a72a7d1581b8f004efe4d9939e99e857"
  }
    search = GoogleSearch(params)
    self.results = search.get_dict()
    return self.results
  
  def GoogleAmazon(self,results):
    #Amazon scraping
    links = []
    for i in range(0,len(results)):
      try:
        if self.Amazon in results['shopping_results'][i]['source']:
          links.append(results['shopping_results'][i]['link'])
        if self.Amazon in results['inline_shopping_results'][i]['source']:
          links.append(results['shopping_results'][i]['link'])
      except:
        pass


 
  def GoogleTarget(self,results):
    #Target scraping
    links = []
    for i in range(0,len(results)):
      try:
        if results['shopping_results'][i]['source'] == self.Target:
          links.append(results['shopping_results'][i]['link'])
        if results['inline_shopping_results'][i]['source'] == self.Target:
          links.append(results['shopping_results'][i]['link'])
      except:
        pass
    return links
  
  
  def GoogleCotsco(self,results):
    #Cosco scraping
    links = []
    for i in range(0,len(results)):
      try:
        if self.Costco in results['shopping_results'][i]['source']:
          links.append(results['shopping_results'][i]['link'])
        if self.Costco in results['inline_shopping_results'][i]['source']:
          links.append(results['shopping_results'][i]['link'])
      except:
        pass
    return links
      

  def GoogleWalmart(self, results):
    #walmart results 
    links = []
    for i in range(0,len(results)):
      try:
          if self.Walmart in results['shopping_results'][i]['source']:
            links.append(results['shopping_results'][i]['link'])
          if self.Walmart in results['inline_shopping_results'][i]['source']:
            links.append(results['shopping_results'][i]['link'])
      except:
        pass
    return links
    









