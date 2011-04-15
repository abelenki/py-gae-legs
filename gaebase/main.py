#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import pygaelegs_cnc

class MainHandler(webapp.RequestHandler):
  def get(self):
    self.response.headers = pygaelegs_cnc.camp_resheaders(self)
    self.response.out.write(pygaelegs_cnc.camp_res_(self))
    
  def post(self):
    self.response.headers = pygaelegs_cnc.camp_resheaders(self)
    self.response.out.write(pygaelegs_cnc.camp_res_(self))

  
class ErrLST(webapp.RequestHandler):
  def get(self):
    self.response.headers["Content-Type"]="text/html"
    self.response.out.write(pygaelegs_cnc.errLST_res_(self))

class ZDebug(webapp.RequestHandler):
  def get(self):
    self.response.headers = pygaelegs_cnc.debug_resheaders(self)
    self.response.out.write(pygaelegs_cnc.debug_res_(self))


def main():
  application = webapp.WSGIApplication(
    [
	  ('/', MainHandler),
	  (r'/zdebug(?:/\w+)*', ZDebug),
	  (r'(?:/\w+)*', MainHandler),
	  (r'(?:/\w+)*.\w+', MainHandler),
	  (r'(?:/\w+)*/', ErrLST)
	], debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
