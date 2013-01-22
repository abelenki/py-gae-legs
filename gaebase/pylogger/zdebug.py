#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# zdebug : it's py-gae-legs' default created stats/debug/log handler
##

  
def show_my_dict_(dict_,title):
  ret_val = "<div><b>" + str(title) + "</b><br/>"
  ret_val = ret_val + str(dict_) + "<br/></div>"
  return ret_val

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
  response = response + show_my_dict_(self.request,"Request")
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
  response = response + "<br/><br/><b>Current Working Dir: " + str(os.getcwd()) + "<br/></b>"
  import sys
  response = response + "<br/>dir(sys): " + str(dir(sys))
  response = response + "<br/><br/><b>Current Platform: " + str(sys.platform) + "<br/></b>"
  response = response + """
    </div><br/><br/>
    <div style="text-align:center;">
      <a href="/">Back To MainPage</a>
    </div>
    </body>
  </html>"""
  return response
  