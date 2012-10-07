#!/usr/bin/python
# -*- coding: utf8 -*-

from lxml import etree
import codecs
import sys

'''
Takes an en strings.xml and a list of translations, and outputs a new
strings.xml file mapping those translations.
'''

if len(sys.argv) != 3:
    print('Usage: strings_generate.py <strings.xml> <translations>')
    sys.exit(1)

def clean_and_check(element):
    if element.text == '':
        return ''
    if '\\n' in original_strings[count] and not '\\n' in element.text:
        print("Warning! '%s' contains linebreaks but translation '%s' "
              "does not" % (original_strings[count], element.text))
    element.text = element.text.replace('...', u'…')
    element.text = element.text.replace('..', u'…')
    return element.text

xml_file = sys.argv[1]
trans_file = sys.argv[2]

tags = []
original_strings = []
translations = []

# Load the tags
with open(xml_file, 'r') as input:
    myxml = input.readlines()
_myxml = [i.lstrip() for i in myxml]
root = etree.fromstring(' '.join(_myxml))
for i in root.findall('string'):
    original_strings.append(i.text)
    tags.append(i.attrib['name'])

# Load the translations
with codecs.open(trans_file, encoding='utf-8', mode='r') as input:
    for line in input.readlines():
        translations.append(line.replace('\n', ''))

if len(translations) != len(tags):
    print("Warning! # translations(%s) != # tags(%s)"
        % (len(translations), len(tags)))

root = etree.Element("resources")
for count, tag in enumerate(tags):
    e = etree.Element("string", name=tag)
    e.text = translations[count]
    if not clean_and_check(e): continue
    root.append(e)

with codecs.open('/tmp/output.xml', encoding='utf-8', mode='w') as outfile:
    outfile.write(etree.tostring(root, pretty_print=True, encoding=unicode))

print('Wrote /tmp/output.xml')
