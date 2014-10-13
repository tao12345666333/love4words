#!/usr/bin/env python
# coding=utf-8
#import tornado

from base import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):
        self.render('home.html',)
