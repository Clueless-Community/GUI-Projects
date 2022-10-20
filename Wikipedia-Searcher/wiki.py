import wikipediaapi

class Wiki:
    """
    This Wiki class have functions for searching wikipedia.
    """

    @staticmethod
    def search_wiki(search:str, words:int=5000) -> str:
        """
        This function searches wikipedia through wikipedia library
         It takes two arguments: 
        search = String data which you want to search about on wikipedia
         sentences = An Integer of how much lines you want data from wikipedia.

        return value = It returns sentences of line as a string.
        """

        wikipedia = wikipediaapi.Wikipedia('en')
        page_py = wikipedia.page(search)
        
        if page_py.exists():
            return f"{page_py.title}\n{page_py.summary[:words]}"
        return "Couldn't find about the given data."
