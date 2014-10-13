import os
import logging

CUR_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = False

TEMPLATE_PATH = os.path.join(CUR_PATH, 'templates')

STATIC_PATH = os.path.join(CUR_PATH, 'static')

SERVER_NAME = 'love'

if os.path.exists(os.path.join(CUR_PATH, '__test__')):
    DEBUG = True

LOG_PATH = '/var/log/'
# log max size per file (bytes)
LOG_MAX_SIZE = 5*1024*1024
LOG_MAX_COUNT = 3

if DEBUG:
    LOG_FILENAME = '%s.log' % SERVER_NAME
else:
    LOG_FILENAME = '%s%s.log' % (LOG_PATH, SERVER_NAME)

# XSRF_COOKIES = True

def _init_logging():
    formatter = logging.Formatter('%(levelname)s:%(asctime)s %(name)s:%(lineno)d:%(funcName)s %(message)s')
    simple_formater = logging.Formatter('%(levelname)s:%(name)s:%(lineno)d:%(funcName)s %(message)s')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # dev log level is debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(simple_formater)

    # file log level is warning mode
    fh = logging.handlers.RotatingFileHandler(
            LOG_FILENAME, maxBytes=LOG_MAX_SIZE, backupCount=LOG_MAX_COUNT)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)


_init_logging()

