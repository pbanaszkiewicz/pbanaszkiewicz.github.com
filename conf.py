# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

SITENAME = 'Blog'
WWW_ROOT = 'http://piotr.banaszkiewicz.org/'
STATIC = ['assets', ]

AUTHOR = 'Piotr Banaszkiewicz'
EMAIL = 'piotr@banaszkiewicz.org'

METASTYLE = "native"
FILTERS = ['reStructuredText', 'hyphenate', 'h2', 'typography']
# FILTERS = ['reStructuredText', 'hyphenate', 'typography']
VIEWS = {
    '/': {'view': 'index', 'pagination': '/page/:num/', 'items_per_page': 5,
    'filters': 'intro+2'},

    '/blog/:year/:month/:day/:slug/': {'views': ['entry', 'draft']},

    '/tags/': {'view': 'tag', 'template': 'tags.html'},
    '/tag/:name/': {'view':'tag', 'pagination': '/tag/:name/:num/'},

    '/atom.xml': {'filters': ['h2', 'nohyphenate'], 'view': 'atom'},
    '/rss.xml': {'filters': ['h2', 'nohyphenate'], 'view': 'rss'},

    '/archive/': {'view': 'archive', 'template': 'archive.html'},

    '/sitemap.xml': {'view': 'sitemap'},

    # # Here are some more examples

    # # '/:slug/' is a slugified url of your static page's title
    '/:slug/': {'view': 'page'},

    # # per tag Atom or RSS feed. Just uncomment to generate them.
    # '/tag/:name/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atompertag'},
    # '/tag/:name/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rsspertag'},

    # # '/atom/full/' will give you a _complete_ feed of all your entries
    # '/atom/full/': {'filters': 'h2', 'view': 'atom', 'num_entries': 1000},

    # # a feed containing all entries tagges with 'python'
    # '/rss/python/': {'filters': 'h2', 'view': 'rss',
    #                  'if': lambda e: 'python' in e.tags}

    # # a full typography features entry including MathML and Footnotes
    # '/:year/:slug': {'filters': ['typography', 'Markdown+Footnotes+MathML'],
    #                  'view': 'entry'}

    # # translations!
    # '/:year/:slug/:lang/': {'view': 'translation'}

    # # search index!
    '/search/': {'view': 'search', 'filters': 'strip+pre'},
}

# SUMMARIZE_LINK = INTRO_LINK = '<a href="%s">&hellip;</a>'

THEME = 'theme'
ENGINE = 'acrylamid.templates.jinja2.Environment'
DATE_FORMAT = '%d.%m.%Y, %H:%M'
LANG = "en_US.utf8"

DISQUS_SHORTNAME = "pbanaszkiewicz"

DEPLOYMENT = {
    "default": "cp CNAME $OUTPUT_DIR; cp .nojekyll $OUTPUT_DIR; ghp-import -b master -p $OUTPUT_DIR",
    "clean": "rm $OUTPUT_DIR -rf",
}
