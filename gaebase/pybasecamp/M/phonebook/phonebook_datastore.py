#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# index_html : it's py-gae-legs' default created index html py file
##

from google.appengine.ext import db


class Phonebook(db.Model):
  #id_ = db.IntegerProperty(required=True)
  timestamp_ = db.DateTimeProperty(auto_now_add=True)
  name = db.StringProperty(required=True)
  phonenumber = db.PhoneNumberProperty(required=False)
  email = db.EmailProperty(required=False)
  description = db.StringProperty(multiline=True)
  
  """ will be trying for auto_id
  def query_counter (q, cursor=None, limit=500):
    if cursor:
      q.with_cursor (cursor)
    count = q.count (limit=limit)
    if count == limit:
      return count + query_counter (q, q.cursor (), limit=limit)
    return count"""