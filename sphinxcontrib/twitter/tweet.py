#-*- coding:utf-8 -*-

from docutils import nodes

from docutils.parsers import rst


class tweet(nodes.General, nodes.Element):
    pass



def visit(self, node):

    tag = u'''<blockquote class="twitter-tweet"><a href="%s">%s</a></blockquote>''' % (node.url, node.url)

    self.body.append(tag)



def depart(self, node):
    pass



class TweetDirective(rst.Directive):

    name = 'tweet'
    node_class = tweet

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}


    def run(self):

        node = self.node_class()

        node.url = self.arguments[0]

        return [node]

