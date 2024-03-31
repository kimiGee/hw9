import unittest
import sys
import pandas as pd
from booklover import BookLover

sys.path.insert(0, '/home/rrp5ut/Documents/MSDS/DS5100/git/hw9/booklover
')

class BookLoverTestSuite(unittest.TestCase):

    booklover1 = BookLover("Sam Smith", "sam@gmail.com", "horror")
    
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`. 
        test_title = "War of the Worlds"
        self.booklover1.add_book(test_title, 4)
        self.assertTrue(self.booklover1.has_read(test_title), "The test value is not present in 'book_list.'")

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_title = "The Giving Tree"
        self.booklover1.add_book(test_title, 5)
        self.booklover1.add_book(test_title, 2)
        self.assertEqual(self.booklover1.book_list['book_name'].value_counts()[test_title], 1)

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_title = "Dracula"
        self.booklover1.add_book(test_title, 4)
        self.assertTrue(self.booklover1.has_read(test_title), "The has_read function did not return True")
        
    def test_4_has_read(self): 
        test_title = "Hex"
        self.assertFalse(self.booklover1.has_read(test_title), "The has_read function did not return False")
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        titles = ["House of Leaves", "Stir of Echos", "The Passage"]
        booklover2 = BookLover("Jane Doe", "jane@gmail.com", "horror")

        for x in titles:
            booklover2.add_book(x, 3) 

        self.assertEqual(booklover2.num_books_read(), len(titles), "The number of books in 'book_list' is not as expected.")
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        fav_titles = ["Stolen Tongues", "How to Sell a Haunted House", "Pet Semetary"]
        other_titles = ["Tender is the Flesh", "Undead Samurai"]
        booklover3 = BookLover("John Doe", "john@gmail.com", "horror")

        for x in fav_titles:
            booklover3.add_book(x, 5) 
        
        for x in other_titles:
            booklover3.add_book(x, 2) 
        
        test_df = booklover3.fav_books()

        #count of returned books with a rating over 3
        returned_from_fav = len(test_df[test_df["book_rating"] > 3])
        
        self.assertEqual(returned_from_fav, len(fav_titles), "The fav_books function did not return the expected number of books")



if __name__ == '__main__':    
    unittest.main(verbosity=3)
    