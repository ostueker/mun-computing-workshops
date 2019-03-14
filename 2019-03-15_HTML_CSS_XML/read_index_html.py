#!/usr/bin/python3
from lxml import etree as ET

my_document = ET.parse('index.html')

for text in my_document.xpath('body/*/text()'):
    print(text) 
