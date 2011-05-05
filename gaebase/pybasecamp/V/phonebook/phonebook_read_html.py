#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# index_html : it's py-gae-legs' default created index html py file
##

from .. import phonebook_main

def get_headers(self):
  headers={"Content-Type":"text/html"}
  return headers 

def get_html(self):
  all_records = str(phonebook_main._read_datastore(self))
  response= """<html>
    <head>
	  <title>py-gae-legs</title>
	</head>
	<body>
	  <div style="text-align:center;">
            <div style="font-size:27px;">Phonebook Records</div>
	    <br/>""" + all_records + """<br/><br/>
	  <div style="text-align:center;">
	    <a href="/phonebook">Phonebook</a>
	  </div>
	</body>
  </html>"""
  return response