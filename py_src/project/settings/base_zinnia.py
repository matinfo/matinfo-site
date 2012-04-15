
### blog main settings
ZINNIA_MEDIA_URL = 'media/blog/'
ZINNIA_COPYRIGHT = 'Django Zinnia\'s Blog'
ZINNIA_UPLOAD_TO = 'uploads'
ZINNIA_PING_DIRECTORIES = ()
ZINNIA_MARKUP_LANGUAGE = "markdown" # textile, restructuredtext (dep. require)

from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS
XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS

### set this in your local settings
AKISMET_SECRET_API_KEY = ''

# bitly short URL
BITLY_LOGIN = ''
BITLY_API_KEY = ''

# twitter API
USE_TWITTER = False
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_KEY = ''
TWITTER_ACCESS_SECRET = ''
