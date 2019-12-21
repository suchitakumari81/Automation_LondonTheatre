'''
Created on Dec 21, 2019

@author: Suchita
'''
from selenium import webdriver
from common.ConfigReader import ConfigReader
from common.JsonParser import JsonParser
from common.ElementNode import *
import os, shutil
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from src.common.ElementNode import TextField, Link, Select, CheckBox, Element, Text, Button


class BaseApplication(object):
    def __init__(self, url=None):
        self.initBaseApp(url)


    def initBaseApp(self, url=None):
        self.browser = ConfigReader().getBrowser()
        self.platform = ConfigReader().getPlatform()
        self.pageUrl = ConfigReader().getUrl()
        self.clearTemp()

        if(self.browser.lower() == 'firefox'):
            firefox_capabilities = DesiredCapabilities.FIREFOX
            firefox_capabilities['marionette'] = True
            firefox_capabilities['handleAlerts'] = True
            firefox_capabilities['acceptSslCerts'] = True
            firefox_capabilities['acceptInsecureCerts'] = True
            geckoPath ='../TestFactory/geckodriver.exe'
            self.driver = webdriver.Firefox(capabilities=firefox_capabilities , executable_path=geckoPath)

        elif(self.browser.lower() == 'ie'):
            desiredCapabilities =webdriver.DesiredCapabilities.INTERNETEXPLORER
            desiredCapabilities.setdefault("nativeEvents",True)
            self.driver = webdriver.Ie()
        elif(self.browser.lower() == 'chrome'):
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            options.add_argument("test-type")
            options.add_argument('start-maximized')
            options.add_argument("--disable-extensions");
            self.driver = webdriver.Chrome(options=options)

        else:

            geckoPath ='../TestFactory/geckodriver.exe'
            self.driver = webdriver.Firefox(executable_path=geckoPath)




        self.driver.maximize_window()
        self.driver.implicitly_wait(40)  # implicit wait for 40 sec
        self.driver.delete_all_cookies()
        self.driver.refresh()


        if(url != None):
            self.driver.get(url)
            self.driver.delete_all_cookies()
            self.driver.refresh()

        else:
            self.driver.get(self.pageUrl)
            self.driver.delete_all_cookies()

            self.driver.refresh()





    def getWebdriver(self):
        return self.driver

    def button(self, elementName):
        locator = JsonParser.getLocator('button', elementName)
        return Button(self.driver, locator)

    def text(self, elementName):
        locator = JsonParser.getLocator('text', elementName)
        return Text(self.driver, locator)

    def element(self, elementName):
        locator = JsonParser.getLocator('element', elementName)
        return Element(self.driver, locator)

    def dropdown(self, elementName):
        locator = JsonParser.getLocator('dropdown', elementName)
        return Element(self.driver, locator)

    def link(self, elementName):
        locator = JsonParser.getLocator('link', elementName)
        return Link(self.driver, locator)

    def textfield(self, elementName):
        locator = JsonParser.getLocator('textfield', elementName)
        return TextField(self.driver, locator)

    def checkbox(self, elementName):
        locator = JsonParser.getLocator('checkbox', elementName)
        return CheckBox(self.driver, locator)

    def select(self, elementName):
        locator = JsonParser.getLocator('select', elementName)
        return Select(self.driver, locator)

    def clearTemp(self):
        folder = 'C:/Temp'

        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                else:
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print("Removing Temp Directory")
            except Exception as e:
                print(e)

