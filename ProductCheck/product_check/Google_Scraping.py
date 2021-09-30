""" 
Scraping multiple ecommerce sites to obtain poduct links using serpAPI

"""

from bs4 import element
from requests import NullHandler
from serpapi import GoogleSearch

class GoogleScraping:
  def __init__(self):
      self.results = {}
      self.Amazon = "Amazon"
      self.Target = "Target"
      self.Costco = "Costco"
      self.Walmart = "Walmart"
      self.apiKey = "4ac8179c2b83da5e87019484de602805a72a7d1581b8f004efe4d9939e99e857"

  def searchQueryShop(self,key,store):
    params = {
      "tbm": "shop",
      "hl": "en",
      "gl": "us",
      "engine": "google",
      "q": key+" "+store,
      "api_key": self.apiKey
  }
    search = GoogleSearch(params)
    self.results = search.get_dict()
    return self.results

  def searchQuery(self,key,store):
      params = {
        "hl": "en",
        "gl": "us",
        "engine": "google",
        "q": key+" "+store,
        "api_key": self.apiKey
    }
      search = GoogleSearch(params)
      self.results = search.get_dict()
      return self.results
  

  def GoogleSearch(self,results,store):
    #Scraping costco results from google search
    #print(results)
    links = []
    def organicResultsInline():
      try:
        organicResults = []
        for i in range(0,len(results["organic_results"])):
          organicResults.append(results["organic_results"][i])
        inlineOrganicResults = organicResults[0]["sitelinks"]["inline"]
        for i in range(0,len(inlineOrganicResults)):
          if store in inlineOrganicResults[i]["link"]:
            links.append(inlineOrganicResults[i]["link"])
      except:
        print("format error in inline organic results")
    def organicresultsExpanded():
      try:
        organicResults = []
        for i in range(0,len(results["organic_results"])):
          organicResults.append(results["organic_results"][i])
        inlineOrganicResults = organicResults[0]["sitelinks"]["expanded"]
        for i in range(0,len(inlineOrganicResults)):
          print(inlineOrganicResults[i]["link"])
          if store in str(inlineOrganicResults[i]["link"]):
            links.append(inlineOrganicResults[i]["link"])
      except:
        print("format error in expanded organic results")
    organicResultsInline()
    organicresultsExpanded()
    return links

  def GoogleSearchShop(self, results,store):
    links = []
    def shoppingResults():
      try:
        for i in range(0,len(results['shopping_results'])):
          print(str(store).strip(".com").upper+str(results['shopping_results'][i]['source']).upper)
          if str(store).strip(".com").upper in str(results['shopping_results'][i]['source']).upper:
            links.append(results['shopping_results'][i]['link'])
      except:
        pass
    def shoppingResultsInline():
      #print(results)
      try:
        for i in range(0,len(results['inline_shopping_results'])):
          if store in results['inline_shopping_results'][i]['source']:
            links.append(results['inline_shopping_results'][i]['link'])
      except:
        pass
    shoppingResults()
    shoppingResultsInline()

    return links









