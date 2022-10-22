import pymongo
from pprint import pprint
import Book
import Review
from pymongo import MongoClient

try:
    client = MongoClient('localhost', 27017)
    print("\nSuccessfully connected!")
except:
    print("\nConnection failed.")
    
db = client.main
books = db.book
reviews = db.review

books.drop()
reviews.drop()

def insertData():
    books.insert_many([Book.b1, Book.b2, Book.b3, Book.b4, Book.b5, Book.b6])
    reviews.insert_many([Review.r1, Review.r2, Review.r3, Review.r4, Review.r5, Review.r6, Review.r7, Review.r8, Review.r9, Review.r10])

def showCollections():
    print("\nPrinting information about collections: ")
    print(db.list_collection_names())

def showBooks():
    print ("\nPrinting information about books:")
    cursor = books.find({})
    for doc in cursor:
        pprint(doc, sort_dicts = False)

def showReviews():
    print("\nPrinting reviews:")
    cursor = reviews.find({})
    for doc in cursor:
        pprint(doc, sort_dicts = False)

def checkBook(title):
    if books.count_documents({"title" : title}) > 0:
        return
    else:
         raise ValueError("The book does not exist")

def authorInformation(title):
    checkBook(title)
    query = {"title" : title}
    doc = books.find(query, {"author"})
    print("\nPrinting information about the author of "+ title +":")
    for i in doc:
        pprint(i, sort_dicts = False)

def reviewCount():
    print("\nInformation about users' review count: \n")
    pipeline = [{"$group" : {"_id" : "$user", "countReviews": {"$count" : {}}}}]
    rows = list(reviews.aggregate(pipeline))
    print(rows)

def reviewCountPrint():
    reviewCount()
    reviewCount_MapReduce()

def reviewCount_MapReduce():
    print("\nInformation about users' review count using map reduce: \n")
    mapF = "function() { emit(this.user, 1) }"  
    reduceF = "function(k, v) { return Array.sum(v)}"  
    result = db.command(
        'mapReduce',  
        'review',
        map = mapF, 
        reduce = reduceF,  
        out = {'inline': 1}  
    )
    print(result)

def main():
    
    insertData()
    while True:
        print("""
        Select the action:
        1 - Show collections
        2 - Show books' data
        3 - Show reviews' data
        4 - Show information about book's author
        5 - Show number of reviews written by user
        6 - Exit
        """)

        action = input('Enter the number of the action: ')
        
        if(action == '1'):
            showCollections()

        elif (action == '2'):
            showBooks()
        
        elif(action == '3'):
            showReviews()
        
        elif(action == '4'):
            title = input("Enter the title of the book: ")
            authorInformation(title)
        
        elif(action == '5'):
            reviewCountPrint()

        elif(action == '6'):
            print("The program is closing...")
            break
        
        else:
            raise ValueError("The action number is incorrect")


if __name__ == '__main__':
    main()
