#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

"""
Client web per www.packtpub.com

@author judith.vimo7@gmail.com
"""
import urllib2
from bs4 import BeautifulSoup
import subprocess


class Client(object):
    # baixar-se la web
    def get_web(self, web_page):
        web = urllib2.urlopen(web_page)
        html = web.read()
        web.close()
        return html

    # buscar el titol del llibre
    def search_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        llibre = soup.find("div", "dotd-title")
        llibre = llibre.text
        solucio = llibre.replace("\t", "")
        solucio = solucio.replace("\n", "")
        return solucio

    def main(self):
        web = (self.get_web\
        ('https://www.packtpub.com/packt/offers/free-learning/'))
        resultat = self.search_text(web)
        subprocess.Popen(["notify-send","Today's book is:" + resultat])


if __name__ == "__main__":
    client = Client()
    client.main()
