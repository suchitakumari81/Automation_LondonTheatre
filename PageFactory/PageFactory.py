from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
        self.full_name = ConfigReader().getValue('full_name')
        self.tel_no = ConfigReader().getValue('tel_no')
        self.primary_email = ConfigReader().getValue('primary_email')
        self.confirm_email = ConfigReader().getValue('confirm_email')
        self.name_on_card = ConfigReader().getValue('name_on_card')
        self.card_number = ConfigReader().getValue('confirm_email')
        self.card_expiry_date = ConfigReader().getValue('card_expiry_date')
        self.cvv_number = ConfigReader().getValue('cvv_number')

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

        # Validate the search item is displayed in result page
        assert self.base.text("result").text() == 'The Simon and Garfunkel Story'
        self.getDriver().execute_script("arguments[0].scrollIntoView();", self.base.button('booking_now_button').getWebElement())
        sleep(10)
        self.base.button('booking_now_button').click()
        self.getDriver().switch_to.window(self.getDriver().window_handles[1])
        # Validate user is navigate to new tab to pick up date of booking
        WebDriverWait(self.getDriver(), 15).until(EC.presence_of_element_located((By.XPATH, "//*[@class='product-booking-header']")))

        assert self.base.text("pick_date_header").getWebElement()
        self.base.button('date_to_pick').click()
        sleep(10)

    def select_seat_to_book(self):
        # Switch to new  iframe and do seat selection
        self.getDriver().switch_to.frame(
        self.getDriver().find_element_by_css_selector('[src="/seatmap/tour-group/7233"]'))
        seat_to_book = self.getDriver().find_elements_by_xpath("//*[name()='circle' and @class='seat bookable']")
        hover = ActionChains(self.getDriver()).move_to_element(seat_to_book[1])
        hover.click().perform()
        sleep(10)
        self.getDriver().switch_to.default_content()

    def navigate_to_next(self):
        self.base.button('next_button').click()

    def fill_on_card_details(self):
        self.base.textfield('full_name').type(self.full_name)
        self.base.textfield('tel_no').type(self.tel_no)
        self.base.textfield('primary_email').type(self.primary_email)
        self.base.textfield('confirm_email').type(self.confirm_email)
        self.base.textfield('name_on_card').type(self.name_on_card)
        self.base.textfield('card_number').type(self.card_number)
        self.base.textfield('card_expiry_date').type(self.card_expiry_date)
        self.base.textfield('cvv_number').type(self.cvv_number)

    def confirm_payment(self):
        self.base.button('confirm_pay_button').click()

    def close(self):
        self.base.driver.quit()
