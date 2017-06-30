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

    def test_comment(self):
        text = get_text()
        counts = test_build_counts(text)
        closest = test_find_closest(text, counts)
        self.assert(len(closest) > 0)



   
