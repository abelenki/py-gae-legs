#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# index_html : it's py-gae-legs' default created index html py file
##

from google.appengine.ext import db
from phonebook_datastore import Phonebook

import os

from google.appengine.ext.webapp import template
#import phonebook_datastore as dstore  
  
def read_(self):
  datab_ = db.GqlQuery("SELECT * FROM Phonebook")
  ret_val = "<div><table><tr>"
  ret_val = ret_val + "<td></td>"
  ret_val = ret_val + "</tr>"
  for record_ in datab_:
    ret_val = ret_val + "<tr>"
    ret_val = ret_val + "<td>" + str(record_.name) + "</td>"
    ret_val = ret_val + "<td>" + str(record_.phonenumber) + "</td>"
    ret_val = ret_val + "<td>" + str(record_.email) + "</td>"
    ret_val = ret_val + "<td>" + str(record_.description) + "</td>"
    ret_val = ret_val + "<td>" + str(record_.timestamp_) + "</td>"
    ret_val = ret_val + "<td>" + str(record_.id_) + "</td>"
    ret_val = ret_val + "<tr>"
  ret_val = ret_val + "</table></div>"
  return ret_val
  
