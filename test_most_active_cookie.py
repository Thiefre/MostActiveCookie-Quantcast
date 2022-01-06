# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:26:15 2021

@author: Kevin Luu
"""

#Run this script using python shell
#Simple black-box testing to see if input/output is correct
import unittest
from most_active_cookie import most_active_cookies



class TestCookies(unittest.TestCase):
    
    def test_different_dates(self):
        f = 'cookie_log.csv'
        self.assertEqual(most_active_cookies('2018-12-09',f), ['AtY0laUfhglK3lC7'])
        self.assertEqual(most_active_cookies('2018-12-08',f), ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'])
        self.assertEqual(most_active_cookies('2018-12-07',f), ['4sMM2LxV07bPJzwf'])
        self.assertEqual(most_active_cookies('2018-12-06',f), [])
    
    def test_invalid_dates(self):
        f = 'cookie_log.csv'
        self.assertEqual(most_active_cookies('test',f), ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf'])
        self.assertEqual(most_active_cookies('',f), ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf'])

    def test_file_inputs(self):
        f = 'dummy_file.txt'
        with self.assertRaises(ValueError):
            most_active_cookies('test',f)
        with self.assertRaises(FileNotFoundError):
            most_active_cookies('test', 'test')
            
if __name__ == '__main__':
    unittest.main()
    