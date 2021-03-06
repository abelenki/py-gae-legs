#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# pygaelegs_cnc : it's py-gae-legs' command-&-control center
#
# it recieves all HTTP Requests from main.py
# and
# forwards all of them to respective controller
##

import re

#index_controller
from pybasecamp.C import index_controller
from pybasecamp.C import phonebook_controller
#debugger/logger/stats-manager
from pylogger import zdebug


def camp_resheaders(self):
  requested_res=self.request.path_qs
  if '/'==requested_res:
    res_header = index_controller.get_headers(self)
  elif re.compile(r'/index(?:/\w+)*').match(requested_res):
    res_header = index_controller.get_headers(self)
  elif re.compile(r'/phonebook(?:/\w+)*').match(requested_res):
    res_header = phonebook_controller.get_headers(self)
  elif re.compile(r'(?:/\w+)*.htm').match(requested_res):
	res_header={"Content-Type":"text/html"}
  else:
    res_header = index_controller.get_headers(self)
  return res_header

def camp_res_(self):
  requested_res=self.request.path_qs
  if '/'==requested_res:
    res = index_controller.get_(self)
  elif re.compile(r'/index(?:/\w+)*').match(requested_res):
    res = index_controller.get_(self)
  elif re.compile(r'/phonebook(?:/\w+)*').match(requested_res):
    res = phonebook_controller.get_(self)
  else:
    res = index_controller.get_(self)
  return res

def campus_res_(self):
  requested_res=self.request.path_qs
  if re.compile(r'/phonebook(?:/\w+)*').match(requested_res):
    res = phonebook_controller.post_(self)
  else:
    res = index_controller.get_(self)
  return res

def debug_resheaders(self):
  debug_head = zdebug.get_headers(self)
  return debug_head

def debug_res_(self):
  debug_data = zdebug.get_(self)
  return debug_data

def errLST_res_(self):
  err_response = """<html>
    <head><title>No Permission</title></head>
	<body>
	  <div style="text-align:center;font-size:23px;">
	    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>
	    You don't have permission to Directory Listing.<br/>
	    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>
		<div style="font-size:32px;">Remove extra '/' from end of URL</div>
		<img src="/images/pygaelegs_error.png" alt="py-gae-legs not available"/><br/>
		<div style="font-size:28px;">to make it work, that's in case if it exists.</div>
	    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>
		If it is supposed to be permitted, notify me at
		<a href="http://github.com/abhishekkr">github.com/abhishekkr</a><br/>
	    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>
	  </div><br/>
	  <div style="text-align:center;">
	    <a href="/">Back To MainPage</a>
	  </div>
	</body>
  </html>"""
  return err_response
