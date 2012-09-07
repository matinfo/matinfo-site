# encoding: utf-8

"""
A filter to highlight code blocks in html with Pygments and BeautifulSoup.

    {% load highlight_code %}

    {{ var_with_code|highlight|safe }}
"""

from BeautifulSoup  import BeautifulSoup
from django import template
from django.template.defaultfilters import stringfilter
import pygments
import pygments.formatters
import pygments.lexers


register = template.Library()

@register.filter
@stringfilter
def highlight(html):
    soup = BeautifulSoup(html)
    codeblocks = soup.findAll('pre')
    for block in codeblocks:
        if block.has_key('class'):
            try:
                code = ''.join([unicode(item) for item in block.contents])
                lexer = pygments.lexers.get_lexer_by_name(block['class'])
                formatter = pygments.formatters.HtmlFormatter()
                code_hl = pygments.highlight(code, lexer, formatter)
                block.contents = [BeautifulSoup(code_hl)]
                block.name = 'code'
            except:
                raise
    return unicode(soup)
