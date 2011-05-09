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
  return """<html>
    <head>
      <title>py-gae-legs ~ PhoneBook</title>
    </head>
    <body>
      <div style="text-align:center;">
        <div style="font-size:27px;">Delete</div>
        <div>
          <span style="font-weight:bold;">PhoneBook</span>
        </div><br/>
        <div>
    """ + str(phonebook_main._delete_datastore(self)) + """
        </div>
      </div><br/>
      <div style="text-align:center;">
        <a href="/phonebook">Delete Entire Phonebook</a>
      </div><br/><br/>
      <div style="text-align:center;">
        <a href="/phonebook">Phonebook</a>
      </div>
    </body>
  </html>"""

def get_list_html(self):
  response= """<html>
    <head>
	  <title>py-gae-legs</title>
	</head>
	<body>
	  <div style="text-align:center;">
            <div style="font-size:27px;">Phonebook Records</div>
	    <br/>""" + str(phonebook_main._delete_list_datastore(self)) + """<br/><br/>
	  <div style="text-align:center;">
	    <a href="/phonebook">Phonebook</a>
	  </div>
	</body>
  </html>"""
  return response
  
  