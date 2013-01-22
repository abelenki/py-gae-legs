#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# index_html : it's py-gae-legs' default created index html py file
##

from phonebook_datastore import Phonebook
from . import phonebook_form

import datetime

#import phonebook_datastore as dstore  

def create_(self):
  return phonebook_form.form_(self, "", "create")
  
def create_list_(self):
  #return str(self.request)
  new_record =  Phonebook(name =str(self.request.get('name')))
  new_record.timestamp_ = datetime.datetime.now()
  new_record.phonenumber = self.request.get('phonenumber')
  new_record.email = self.request.get('email')
  new_record.description = self.request.get('description')
  new_record.put()  #saving 
  return " [[New Record Added]] <br/>~~~~~~~~~~<br/> "  + phonebook_form.static_form_(self, new_record.key())
  