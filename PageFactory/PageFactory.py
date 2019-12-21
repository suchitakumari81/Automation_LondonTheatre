from time import sleep


from common.BaseApplication import BaseApplication, ActionChains, EC
from common.ConfigReader import ConfigReader


class BasePageClass(object):
    isInitialized = False
    base = None

    def __init__(self, url=None):
        if (BasePageClass.isInitialized == False):
            if (url == None):
                BasePageClass.base = BaseApplication()
            else:
                BasePageClass.base = BaseApplication(url)

            BasePageClass.isInitialized = True
            print("Initialized the base application..")
        else:

            print("Already initialized...")

    def getDriver(self):

        return self.base.getWebdriver()

    def getScreenshots(self, images):  # Method to Store Screenshot on failures

        Browser = self.base.browser
        Report = "../TestFactory/Snapshots/" + str(Browser) + str('/ActualScreenshots/') + str(images)
        print("Report dir is \t" + str(Report))
        self.getDriver().save_screenshot(Report)


class BookingHomePage(BasePageClass):
    def __init__(self, url=None):
        self.search_for_tickets = ConfigReader().getValue('search_for_tickets')
        BasePageClass.isInitialized = False
        BasePageClass.__init__(self, url)


    def search_for_story(self):
        self.base.textfield('search_tickets').type(self.search_for_tickets)

        # Validation of searched story found for ticket bookings
        assert self.base.element("go_to_search_resulted_page").getWebElement()

    def navigate_book_now_page(self):
        theatre_element = self.base.element('go_to_search_resulted_page').getWebElement()
        # hover on the element to get the book now button click
        hover = ActionChains(self.getDriver()).move_to_element(theatre_element)
        hover.click().perform()
        assert self.base.text("Result").text() == 'The Simon and Garfunkel Story'
        self.getDriver().execute_script("arguments[0].scrollIntoView();",
                                        self.base.button('booking_now_button').getWebElement())
        sleep(20)
        self.base.button('booking_now_button').click()
        sleep(20)
        self.getDriver().switch_to.window(self.getDriver().window_handles[1])
        # Validate user is navigate to new tab to pick up date of booking
        assert self.base.text("Pick_date_header").getWebElement()
        self.base.button('date_to_pick').click()
        sleep(10)

    def select_seat_to_book(self):
        # Switch to iframe for seat selection
        self.getDriver().switch_to.frame(self.getDriver().find_element_by_css_selector('[src="/seatmap/tour-group/7233"]'))
        seat_to_book = self.getDriver().find_elements_by_xpath("//*[name()='circle' and @class='seat bookable']")
        hover = ActionChains(self.getDriver()).move_to_element(seat_to_book[1])
        hover.click().perform()
        sleep(20)
        self.getDriver().switch_to.default_content()
    def navigate_to_next(self):

        self.base.button('next_button').click()


    def close(self):
        self.base.driver.quit()
