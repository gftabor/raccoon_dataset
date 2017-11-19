#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 02:21:39 2017

@author: gtabor
"""

import xml.etree.ElementTree

# Open original file
for i in range(200):
    name = 'annotations/raccoon-' + str(i+1) + '.xml'
    et = xml.etree.ElementTree.parse(name)
    root = et.getroot()
    root[1].text=root[1].text[:-3] + 'jpg'
    
    root[2].text=root[2].text[:-3] + 'jpg'
    print(root[2].text)
    
    
    # Write back to file
    #et.write('file.xml')
    et.write(name)