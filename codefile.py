## importing library for manipulating data frame
import pandas as pd

## importing library to getting url
import requests
from requests import get
## beautiful soup library which makes text parsing and simple
from bs4 import BeautifulSoup

class imdb(object):
    def getting_url(self):
      response = get('http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1')
      html_soup = BeautifulSoup(response.text, 'html.parser')
      return html_soup

    def movie_data(self):
      html_soup=self.getting_url()
      movie_containers =html_soup.find_all('div', class_ = 'lister-item mode-advanced')
      return movie_containers
## function for creating the lists of years,movie-titles,year of release,lenght of movie,imdb,meta scores
    def columns_data(self):
        movie_containers=self.movie_data()
        names=[]
        years=[]
        length=[]
        genres=[]
        imdb_scores=[]
        meta_scores=[]
        for i in range(0,len(movie_containers)):
            title= movie_containers[i].h3.a.text
            names.append(title)
            year=movie_containers[i].h3.find('span', class_ = 'lister-item-year text-muted unbold').text
            years.append(year)
            len_=movie_containers[i].p.find('span',class_="runtime").text
            length.append(len_)
            genre=movie_containers[i].p.find('span',class_="genre").text
            genres.append(genre)
            imdb=movie_containers[i].strong.text
            imdb_scores.append(imdb)
            meta= movie_containers[i].find('span',class_="metascore favorable")
            if meta is not None:
                metatext = meta.get_text(strip=True)
                meta_scores.append(metatext)
            else:
                meta_scores.append('None')
        return names,years,length,genres,imdb_scores,meta_scores
    
def main():
     imdbObj = imdb()
     names,years,length,genres,imdb_scores,meta_scores = imdbObj.columns_data()
     df=pd.DataFrame(data={"movie-name":names,"release_year":years,"time":length,"imdb":imdb_scores,"metascore":meta_scores}     

## Printing the first 20 lines of the data frame    
    print(df.head(20))
    
if __name__=="__main__":
    main()
