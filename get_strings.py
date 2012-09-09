#!/usr/bin/python

'''
Takes an en strings.xml and outputs the bare strings.
Use to seed a new Google Doc.
'''

from lxml import etree
import codecs
import sys

xml_file = sys.argv[1]

# Load the tags
with open(xml_file, 'r') as input:
    myxml = input.readlines()
_myxml = [i.lstrip() for i in myxml]
root = etree.fromstring(' '.join(_myxml))
for i in root.findall('string'):
    print(i.text).encode('utf-8')
