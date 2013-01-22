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
        <div style="font-size:27px;">PhoneBook</div>
        <div>
          <span style="font-weight:bold;">CRUD Pages</span>
        </div><br/><br/>
        <div>
          <a href="/phonebook/V/create">Create 'PhoneBook' Entry</a><br/><br/>
          <a href="/phonebook/V/read">Read Entire 'PhoneBook'</a><br/><br/>
          <a href="/phonebook/V/update">Update 'PhoneBook' Entry</a><br/><br/>
          <a href="/phonebook/V/delete">Delete 'PhoneBook' Entry</a><br/>
        </div>
      </div><br/><br/>
      <div style="text-align:center;">
        <a href="/">Homepage</a>
      </div>
    </body>
  </html>"""
  
#####end=of=phonebook_html