from logging import basicConfig, getLogger, StreamHandler, DEBUG, ERROR, INFO
import sys


basicConfig()
logger = getLogger('MulTweetTwitter')
logger.setLevel(INFO)


log = logger.log
