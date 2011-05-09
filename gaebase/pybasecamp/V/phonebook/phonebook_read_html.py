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
  response= """<html>
    <head>
	  <title>py-gae-legs</title>
	</head>
	<body>
	  <div style="text-align:center;">
            <div style="font-size:27px;">Phonebook Records</div>
	    <br/>""" + str(phonebook_main._readform_datastore(self)) + """<br/><br/>
	  <div style="text-align:center;">
	    <a href="/phonebook">Phonebook</a>
	  </div>
	</body>
  </html>"""
  return response

def get_list_html(self):
  response= """<html>
    <head>
	  <title>py-gae-legs</title>
	</head>
	<body>
	  <div style="text-align:center;">
            <div style="font-size:27px;">Phonebook Records</div>
	    <br/>""" + str(phonebook_main._read_list_datastore(self)) + """<br/><br/>
	  <div style="text-align:center;">
	    <a href="/phonebook">Phonebook</a>
	  </div>
	</body>
  </html>"""
  return response