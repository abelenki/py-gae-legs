#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# zdebug : it's py-gae-legs' default created stats/debug/log handler
##

def get_headers(self):
  headers={"Content-Type":"text/html"}
  return headers 

def get_(self):
  response ="""<html>
    <head>
      <title>aLabs</title>
    </head>
    <body>
      <div class="debug_mode_info" style="text-align:center;">
	  """
  response = response + str(self.request.path_qs)
  response = response + "<br/>Path: " + str(self.request.path)
  response = response + "<br/>Path URL: " + str(self.request.path_url)
  response = response + "<br/>Host: " + str(self.request.host)
  response = response + "<br/>Host URL: " + str(self.request.host_url)
  response = response + "<br/>App URL: " + str(self.request.application_url)
  response = response + "<br/>Body: " + str(self.request.body)
  response = response + "<br/>Body File: " + str(self.request.body_file)
  response = response + "<br/>Query String: " + str(self.request.query_string)
  response = response + "<br/>Query Vars: " + str(self.request.queryvars)
  response = response + "<br/>Query Value for 'id' would be at str(self.request.queryvars['id'])"
  from google.appengine.api import users
  user=users.get_current_user()
  response = response + "<br/>dir(users): " + str(dir(users))
  if user:
    response = response + "<br/>Current User: " + str(user)  
  else:
    self.redirect(users.create_login_url(self.request.uri))
  import os
  response = response + "<br/>dir(os): " + str(dir(os))
  response = response + "<br/>Current Working Dir: " + str(os.getcwd())
  import sys
  response = response + "<br/>dir(sys): " + str(dir(sys))
  response = response + "<br/>Current Platform: " + str(sys.platform)
  response = response + "<br/><br/>" + str(dir(self.request))
  response = response + """
	  </div><br/><br/>
	  <div style="text-align:center;">
	    <a href="/">Back To MainPage</a>
	  </div>
    </body>
  </html>"""
  return response