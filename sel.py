import json
import re
import string

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class sel:

    def __init__(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_prefs = {}
        # chrome_options.experimental_options["prefs"] = chrome_prefs
        # chrome_prefs["profile.default_content_settings"] = {"images": 2}
        # chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        # self.driver = webdriver.Chrome(options=chrome_options)
        pass

    def go_to_page(self, url):
        self.driver.get(url)

    def get_current_week(self, xpath):
        web_element = self.driver.find_element_by_xpath(xpath)
        return int((re.findall('\d+', web_element.text)[0]))

    def read_team(self, xpath):
        web_element = self.driver.find_element_by_xpath(xpath)
        return web_element.text

    def read_sum_points(self, xpath):
        web_element = self.driver.find_element_by_xpath(xpath)
        return int((re.findall('\d+', web_element.text)[0]))

    def get_team_number(self, xpath):
        web_elements = self.driver.find_elements_by_xpath(xpath)
        return web_elements.__len__()

    def sort_two_lists(self, list1, list2):
        list_sorted_1, list_sorted_2 = zip(*sorted(zip(list2, list1), reverse=True))

        # zipped_lists = zip(list1, list2)
        # sorted_pairs = sorted(zipped_lists)
        #
        # tuples = zip(*sorted_pairs)
        # list_sorted_1, list_sorted_2 = [list(tuple) for tuple in tuples]
        return list_sorted_1, list_sorted_2

    def write_file(self, list):
        # define list with values
        # open output file for writing
        with open('data.json', 'w') as filehandle:
            json.dump(list, filehandle)

    def read_file(self, filename):
        with open(filename, 'r') as filehandle:
            return json.load(filehandle)

    def teardown(self):
        self.driver.close()
        self.driver.quit()
