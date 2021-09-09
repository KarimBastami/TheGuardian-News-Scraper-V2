import pymongo


def initializeUserInterface():
    print("")
    print("# ----------------------- #")
    print("# ------ Main Menu ------ #")
    print("# ----------------------- #")
    print("")
    print("0: Search For Articles")
    print("--------------------------")
    print("")



def getArticlesUsingCategory(_collection, _category):
    return list(_collection.find({
         "$or": [
                 {"Category": {"$regex" : _category}}, 
                 {"Text Content": {"$regex" : _category}},
                 {"Title": {"$regex" : _category}}
                ]
                                }))




# ----------------------------------- #
# -------------   Main  ------------- #
# ----------------------------------- #


client = pymongo.MongoClient("mongodb+srv://Scrapy_Scraper:BNPKPhu6WpStzAfw@theguardianarticles.zaufd.mongodb.net/TheGuardianArticles?retryWrites=true&w=majority")

db = client["TheGuardian"]
collection = db["News_Articles"]

# ------------------------------------------------------------------------------------------------------------


initializeUserInterface()

choice = input("Enter your choice (0 - 0): ")

    
if (choice == "0"):

    categoryInput = input("\nEnter category criteria: ")
    filteredArticlesList = getArticlesUsingCategory(collection, categoryInput)

    dbArticleCount = collection.count_documents({})
    filteredArticlesCount = len(filteredArticlesList)

    
    if (len(filteredArticlesList) > 0):

        for element in filteredArticlesList:
            print("\n\n---------------------------------------------------------------------------------------------")
            print("Title:", element["Title"])
            print("\nCategory:", element["Category"])
            print("\nArticle Type:", element["Article Type"])
            print("\nAuthor:", element["Author"])
            print("\nUrl:", element["Url"])
            print("\nText Content:\n\n" + element["Text Content"])
            print("---------------------------------------------------------------------------------------------\n")
    else:
        print("\nNo articles with a category of", categoryInput, "found!\n")

    
    print("Total number of available articles:", dbArticleCount)
    print("\nTotal number of articles with criteria of", categoryInput + ":", filteredArticlesCount)
    print("---------------------------------------------------------------------------------------------\n")


else:
    print("")
    print("Please select a valid option (0-0) \n")