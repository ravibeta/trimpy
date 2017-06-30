#! /usr/bin/python3
#
from abc import ABCMeta, abstractmethod

class Summarizer(object):
    """A Summarizer for text as a strategy

    Attributes:
    """

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def summarize(self):
        pass
