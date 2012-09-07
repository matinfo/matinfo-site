from django.db import models
from django.utils.html import linebreaks

from zinnia.models import EntryAbstractClass
from zinnia.settings import MARKUP_LANGUAGE
from zinnia.settings import MARKDOWN_EXTENSIONS

from django.contrib.markup.templatetags.markup import markdown
from django.contrib.markup.templatetags.markup import textile
from django.contrib.markup.templatetags.markup import restructuredtext

class Entry(EntryAbstractClass):

    @property
    def html_excerpt(self):
        """Return the Entry.content attribute formatted in HTML"""
        if MARKUP_LANGUAGE == 'markdown':
            return markdown(self.excerpt, MARKDOWN_EXTENSIONS)
        elif MARKUP_LANGUAGE == 'textile':
            return textile(self.excerpt)
        elif MARKUP_LANGUAGE == 'restructuredtext':
            return restructuredtext(self.excerpt)
        elif not '</p>' in self.excerpt:
            return linebreaks(self.excerpt)
        return self.excerpt

    class Meta(EntryAbstractClass.Meta):
        abstract = True
