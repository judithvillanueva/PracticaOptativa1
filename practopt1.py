#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

"""
Client web per www.packtpub.com

@author judith.vimo7@gmail.com
"""
import urllib2


class Client(object):
    # baixar-se la web
    def get_web(self, web_page):
        web = urllib2.urlopen(web_page)
        html = web.read()
        web.close()
        return html

    def main(self):
        resultat = (self.get_web\
        ('https://www.packtpub.com/packt/offers/free-learning/'))
        print resultat


if __name__ == "__main__":
    client = Client()
    client.main()
