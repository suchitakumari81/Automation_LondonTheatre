'''
Created on Dec 21, 2019

@author: Suchita
'''
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Node(object):
    def loadConfigDetails(self):
        tree = ET.parse('elements.xml')
        self.root = tree.getroot()
        print (self.root.tag)
        print (self.root.attrib)

        for nodes in self.root.findall("node"):
            expected = 'text'
            actual = nodes.get('id')
            if actual == expected:
                for elts in nodes.findall('entry'):
                    print(elts.get('key'))
                    print(elts.get('value'))

    def __init__(self):
        self.webElement = None

    def getElement(self, driver, locator):
        if(locator.startswith('id=')):   #return driver.find_element_by_id(loc[1])
            loc = locator.split("id=")
            return WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, loc[1])))

        if(locator.startswith('xpath=')):  #return driver.find_element_by_xpath(loc[1])

            loc = locator.split("xpath=")
            return WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, loc[1])))

        if(locator.startswith('css=')): #return driver.find_element_by_css_selector(loc[1])
            loc = locator.split("css=")
            return WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, loc[1])))

        if(locator.startswith('link=')):
            loc = locator.split("link=")
            return WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, loc[1])))
            #return driver.find_element_by_partial_link_text(loc[1])

        if(locator.startswith('class=')):  #return driver.find_element_by_class_name(loc[1])
            loc = locator.split("class=")
            return WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME ,loc[1])))


        if(locator.startswith('name=')): #return driver.find_element_by_name(loc[1])
            loc = locator.split("name=")
            return WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME ,loc[1])))



    def click(self):
        self.webElement.click()

    def text(self):
        return self.webElement.text

    def getWebElement(self):
        return self.webElement

    def type(self, val):
        self.webElement.clear()
        self.webElement.send_keys(val)

    def getAttribute(self,name):
        return self.webElement.get_attribute(name)
    
    def getName(self, name):
        return self.webElement.get_name()
    
    def clickAndHold(self):
        self.webElement.click_and_hold()
        
        

class Button(Node):
    def __init__(self, wd, locator):
        Node.__init__(self)
        self.webElement = self.getElement(wd, locator)


class Text(Node):
    def __init__(self, wd, locator):
        Node.__init__(self)
        self.webElement = self.getElement(wd, locator)

class TextField(Node):
    def __init__(self, wd, locator):
        Node.__init__(self)
        self.webElement = self.getElement(wd, locator)

class CheckBox(Node):
    def __init__(self, wd, locator):
        Node.__init__(self)
        self.webElement = self.getElement(wd, locator)

class Select(Node):
    def __init__(self, wd, locator):
        Node.__init__(self)
        self.webElement = self.getElement(wd, locator)

class Element(Node):
    def __init__(self, wd, locator):
        Node.__init__(self)
        self.webElement = self.getElement(wd, locator)

class Dropdown(Node):
    def __init__(self, wd, locator):
        Node.__init__(self)
        self.webElement = self.getElement(wd, locator)

class Link(Node):
    def __init__(self, wd, locator): 
        Node.__init__(self)
        self.webElement = self.getElement(wd, locator)
