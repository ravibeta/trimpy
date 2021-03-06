#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
import warnings
import json
from trimpy.summarizers.selector import Selector


class TestSelector(unittest.TestCase):

    def setUp(self):
        pass

    def get_text():
        with open('test.txt', 'r') as fin:
             text = fin.readlines()
        text = '\n'.join(text)
        return text


    def test_comment(self):
        text = self.get_text()
        p = Selector()
        closest = p.summarize(text)
        self.assert(len(closest) > 0)



   
