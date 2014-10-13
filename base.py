#!/usr/bin/env python
# coding=utf-8
import tornado.web

#import loggers

#loggers = loggers.getLogger(__file__)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.session['user'] if self.session and 'user' in self.session else None
