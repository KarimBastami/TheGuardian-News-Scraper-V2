# TheGuardian-News-Scraper-V2

- A better and improved version of my news scraper using Scrapy spiders and MongoDB 
- This scraper only targets articles from TheGuardian.com

Scraped Information include:
  - Title
  - URL
  - Category
  - Article Type
  - Author
  - Text Content

### How To Use:

- This project is split into two parts 
  - Scraper
  - Mongo Queries: Article retrieval based on a search critera

Scraper Part:
  - From a command line or terminal change directory to Scrapy_News_Scraper / news_scraper
  - In the command line type ```scrapy crawl theguardian ```  (this will start the scraping process for all the articles on theguardian and upload them to MongoDB)

Mongo Queries:
  - Run main.py and a console based user interface for article searching should appear 
 
Custom MongoDB Client:
  - If you wish to upload to ur own MongoDB Database then do the following
    - Navigate to the Pipeline.py file 
    - Replace
    
     ```python
     self.client = pymongo.MongoClient("mongodb+srv://Scrapy_Scraper:BNPKPhu6WpStzAfw@theguardianarticles.zaufd.mongodb.net/TheGuardianArticles?retryWrites=true&w=majority") 
     ```
     with your own Mongo client 

  
### Main Features:
  - Supports link crawling and iterating through pagination to gather all the articles
  - Proper identification of article types and accordingly changing scraping criteria
  - Simple console based user interface to retrieve and read articles based on the user's criteria of choice
  
 
### Tools Used:
  - Scrapy
  - MongoDB 
  - Pymongo and Dnspython libraries
  
  
 
 
