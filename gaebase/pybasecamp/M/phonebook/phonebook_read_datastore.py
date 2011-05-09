#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# index_html : it's py-gae-legs' default created index html py file
##

from google.appengine.ext import db

from phonebook_datastore import Phonebook
from . import phonebook_form
#import phonebook_datastore as dstore  
  
def read_(self):
  requested_res=self.request.path_qs
  record_key=requested_res.split("/")[-1]
  return phonebook_form.static_form_(self,  record_key)
  
def read_list_(self):
  return phonebook_form.static_list_(self, "read")
  
