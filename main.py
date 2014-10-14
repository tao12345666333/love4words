import tornado.web
import tornado.httpserver
import tornado.options

from tornado.options import define, options
import setting
from apps import urlpatterns

define('port', default=9999, type=int)

class Application(tornado.web.Application):
    def __init__(self):
        hanlers = urlpatterns

        settings = dict(
            template_path = setting.TEMPLATE_PATH,
            static_path = setting.STATIC_PATH,
            debug = setting.DEBUG
            )

        tornado.web.Application.__init__(self, hanlers, **settings)

def main():
    print 'system started ...'
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(),xheaders=True)
    http_server.listen(options.port)
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.start()

if __name__== '__main__':
    main()
