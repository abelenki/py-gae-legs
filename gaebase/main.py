#!/usr/bin/env python
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
    self.response.out.write(pygaelegs_cnc.campus_res_(self))


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
