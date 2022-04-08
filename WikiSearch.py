import wikipediaapi

class WikiSearch:
    def find_wiki(toSearch):
        wiki = wikipediaapi.Wikipedia('en')
        findPage = wiki.page(toSearch.split(',')[0:1])
        return findPage.fullurl
