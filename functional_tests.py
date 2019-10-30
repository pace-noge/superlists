#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has jeard about a cool new online to-do app. She goes
        # to check it out its homepage
        self.browser.get("http://localhost:8000")

        # She notice the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)


        # She is invited to enter a to-do item straight away
        input_box = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            "Enter a to-do item"
        )


        # she types "Buy peacock feathers" into a text box (Edit's hobby)
        # is tying fly-fishing lures
        input_box.send_keys("Buy peacock feathers")


        # When she hit enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )


        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make fly" (Edith is very methodical)


        # The page updates again, now show both item on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

        self.fail('Finish the test.')


if __name__ == "__main__":
    unittest.main(warnings='ignore')

