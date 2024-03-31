
import pandas as pd

class BookLover():

    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

    def __init__(self, name, email, fav_genre):

        self.name = name
        self.email = email
        self.fav_genre = fav_genre


    def add_book(self, book_name, rating):

        if self.has_read(book_name):
            return "This book is already in your book list."
        
        new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [rating]
        })

        self.num_books+=1

        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)

        return "Book successfuly added."
    

    def has_read(self, book_name):

        return self.book_list['book_name'].eq(book_name).any()
    
    
    def num_books_read(self):

        return self.num_books
    
    def fav_books(self):

        return self.book_list[self.book_list['book_rating'] > 3]
    
   



def main(): 
    """
   test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
   print(test_object.add_book("War of the Worlds", 4))
   print(test_object.add_book("Where is my Hat", 5))
   print(test_object.add_book("Fourth Wing", 2))
   print(test_object.add_book("The Giving Tree", 5))
   print(test_object.add_book("The Cloisters", 3))
   print("favorite books:", test_object.fav_books())
   print("Number of books read:", test_object.num_books_read())
  
"""
    


if __name__ == '__main__':    
    main()
  