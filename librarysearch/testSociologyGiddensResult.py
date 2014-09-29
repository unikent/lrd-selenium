#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class testSociologyGiddensResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox", "http://pmt-eu.hosted.exlibrisgroup.com/")
        self.selenium.start()
    
    def test_test_sociology_giddens_result(self):
        sel = self.selenium
        sel.open("/primo_library/libweb/action/search.do?vid=44KEN_VU1&reset_config=true")
        sel.type("id=search_field", "giddens sociology")
        sel.click("id=goButton")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Sociology", sel.get_text("css=span.searchword"))
        self.assertEqual("Anthony Giddens", sel.get_text("css=h3.EXLResultAuthor"))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
