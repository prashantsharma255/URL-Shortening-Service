from django.conf import settings
from django_hosts import patterns, host
from kirr.hostsconf import urls as redirect_urls

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', redirect_urls , name='wildcard'),
)

'''
from kirr.hostconf import urls as redirect_urls
host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', redirect_urls, name='wildcard'),
)
'''