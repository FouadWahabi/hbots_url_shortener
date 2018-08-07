# -*- coding: utf-8 -*-

from url_shortener.views.frontend import frontend, IndexView, ShortLinkRedirectView, RestAPI

routes = [
    ((frontend, ''),
        ('/', IndexView.as_view('index')),
        ('/<short_code>', ShortLinkRedirectView.as_view('redir')),
    ),
]

apis = [
    ('/api', RestAPI)
]
