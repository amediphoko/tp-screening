'''
Created on 26 Sep 2018

@author: adiphoko
'''
from edc_identifier.simple_identifier import SimpleUniqueIdentifier


class ScreeningIdentifier(SimpleUniqueIdentifier):
    identifier_type = 'screening_identifier'
    template = 'S{device_id}{random_string}'
