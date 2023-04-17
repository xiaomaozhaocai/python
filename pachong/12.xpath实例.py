#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from lxml import etree
if __name__ == '__main__':
    tree = etree.parse('cat.html')
    r = tree.xpath('/html/head/title')
    print(r)