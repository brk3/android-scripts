#!/usr/bin/python

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

xml_file = sys.argv[1]
trans_file = sys.argv[2]

tags = []
translations = []

# Load the tags
with open(xml_file, 'r') as input:
    myxml = input.readlines()
_myxml = [i.lstrip() for i in myxml]
root = etree.fromstring(' '.join(_myxml))
for i in root.findall('string'):
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
    # don't add empty entries, android should fall back to english translation
    if e.text == '': continue
    root.append(e)

with codecs.open('/tmp/output.xml', encoding='utf-8', mode='w') as outfile:
    outfile.write(etree.tostring(root, pretty_print=True, encoding=unicode))

print('Wrote /tmp/output.xml')
