#!/usr/bin/env python3
# encoding: utf-8


import os
import sys
import requests
from bs4 import BeautifulSoup
import logging
import cookielib
import mechanize


logging.getLogger(__name__)


class Dcard:
    account = 'obsidiany@gmail.com'
    password = 'login12345'
    base_url = 'https://www.dcard.tw/'

    def __init__(self):
        self.br = mechanize.Browser()
        self.br.set_cookiejar(cookielib.CookieJar())

    def fetch(self, url):
        self.br.open(base_url)
        for ff in self.br.forms():
            print("parsed ok")
            import pdb
            pdb.set_trace()
            parsed = BeautifulSoup(ff, 'html.parser')



def main():
    dcard = Dcard()
    dcard.fetch('https://www.dcard.tw/')


if __name__ == '__main__':
    main()
