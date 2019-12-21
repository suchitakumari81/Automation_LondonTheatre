'''
Created on Dec 21, 2019

@author: Suchita
'''
import os
import unittest
from PageFactory.PageFactory import BookingHomePage
from common.ConfigReader import ConfigReader
import HtmlTestRunner


class TestLondanTheatre(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("current working directory", os.getcwd());
        self.url = ConfigReader().getValue('baseUrl')
        self.page = BookingHomePage(self.url)

        pass

    @classmethod
    def tearDownClass(self):
        self.page.close()
        print("Booking of Tickets The Simon and Garfunkel Story Test Ended")

    def test_story_booking_Ticket(self):
        # Search for search_for_tickets for the story "The Simon and Garfunkel Story ""
        self.page.search_for_story()
        self.page.navigate_book_now_page()
        self.page.select_seat_to_book()
        self.page.navigate_to_next()

    pass

    if __name__ == '__main__':

        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./Reports'))
