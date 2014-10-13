#!/usr/bin/env python
# coding=utf-8
import tornado.web
#from apps import base
from setting import TEMPLATE_PATH

class BaseHandler(tornado.web.RequestHandler):
    #def initialize(self):
    #    super(BaseHandler, self).initialize()
    #    self.template_path = TEMPLATE_PATH
    #    self._params = self.parameter

    def get_context(self):
        context = super(BaseHandler, self).get_context()
        context.update({

        })

        return context
