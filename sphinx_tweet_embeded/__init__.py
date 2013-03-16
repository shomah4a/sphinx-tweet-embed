#-*- coding:utf-8 -*-

__version__ = '0.1.0'
__author__ = '@shomah4a'
__license__ = 'GPLv3'


from . import tweet


def setup(app):

    app.add_node(tweet.tweet,
                 html=(tweet.visit, tweet.depart))
    app.add_directive('tweet', tweet.TweetDirective)

