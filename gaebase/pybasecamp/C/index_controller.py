#!/usr/bin/env python### https://github.com/abhishekkr/py-gae-legs## index_controller : it's py-gae-legs' default created index file##from ..V.index import index_htmldef get_headers(self):  return index_html.get_headers(self)def get_(self):  return index_html.get_html(self)