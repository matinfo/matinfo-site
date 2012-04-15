from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

#handler404 = "project.views.page_not_found"
#handler500 = "project.views.server_error"

# zinnia sitemaps URLs
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

urlpatterns = patterns('',
    ('^$', 'django.views.generic.simple.redirect_to', {'url': '/blog/'}),
    (r'^blog/', include('zinnia.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),

    (r'^admin/login-as/', include('login_as.urls')),
    (r'^admin/', include(admin.site.urls)),
#    (r'^i18n/setlang/$', 'django.views.i18n.set_language'),
#    (r'^tinymce/', include('tinymce.urls')),
    (r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
)

sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap,
}

urlpatterns += patterns('django.contrib.sitemaps.views',
    (r'^blog/sitemap.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^blog/sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)

if settings.IS_DEV_SERVER:
    if 'appmedia' in settings.INSTALLED_APPS:
        urlpatterns = patterns('',
            (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
        ) + urlpatterns
    else:
        urlpatterns = patterns('',
            (r'^' + settings.MEDIA_URL.lstrip('/') + '(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + urlpatterns
    if settings.IS_HTTP_SERVER:
        urlpatterns += patterns('',
            (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + '../', 'show_indexes': True}),
        )
