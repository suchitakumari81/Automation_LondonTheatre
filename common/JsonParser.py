'''
Created on Dec 21, 2019

@author: suchita
'''
import json
from fileinput import close


class JsonParser(object):

    @staticmethod
    def is_file_open(file):
        try:
            json_data = open(file)
            json_data.close()
            return False

        except IOError:
            return json_data

    @staticmethod
    def getValidJsonObj(json_data):
        try:
            return json.load(json_data)
        except:
            return False

    @staticmethod
    def getLocator(node_type, elementName):
        json_data = JsonParser.is_file_open('../config/elements.json')
        if json_data:
            json_data.close()

        json_data = open("../config/elements.json")
        json_obj = JsonParser.getValidJsonObj(json_data)

        if not json_obj:
            print("Failed while parsing the json file\n")
            exit(-1)

        for node in json_obj:
            for node_name in node:
                print(node_name)
                val = None
                if node_name == node_type:
                    for val in node[node_type]:
                        for elt_name in val:
                            if elt_name == elementName:
                                print(val)
                                return val[elementName]