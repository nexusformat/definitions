# -*- coding: utf-8 -*-
"""
    nexus_blockquote_css.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    Modify the defaults for blockquotes (especially: set margin-right to zero)
"""

from docutils import nodes

def setup(app):
    app.add_stylesheet('_static/blockquote.css')
