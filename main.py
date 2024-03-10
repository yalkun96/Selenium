import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.path = "/Users/zzzzzz/Downloads/chromedriver-mac-arm64/chromedriver"
        self.driver = webdriver.Chrome()
        self.driver.get('https://cz.careers.veeam.com/vacancies')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # seconds

    def test(self):
        coockie = self.driver.find_element(By.ID, 'cookiescript_accept')
        coockie.click()

        choose_jobs_list = self.driver.find_element(By.ID, 'sl')
        choose_jobs_list.click()

        choosle_research_and_development = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Research')
        choosle_research_and_development.click()

        find_jobs = self.driver.find_elements(By.CLASS_NAME, 'card')

        expected_value = 15

        if len(find_jobs) == expected_value:
            print(f'Number of jobs counted: {len(find_jobs)} corresponds to expected value: {expected_value}')
        else:
            print(f'Number of jobs counted: {len(find_jobs)} does not correspond to expected value: {expected_value}')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()