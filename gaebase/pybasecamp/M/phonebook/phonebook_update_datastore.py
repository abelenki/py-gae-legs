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

def update_form(self):
  requested_res=self.request.path_qs
  record_key=requested_res.split("/")[-1]
  return phonebook_form.form_(self, record_key, "update")
  
def update_(self):
  requested_res=self.request.path_qs
  record_key=requested_res.split("/")[-1]
  if(record_key):
    record_=Phonebook.get(record_key)
    record_.name =  str(self.request.get('name'))
    record_.timestamp_ = datetime.datetime.now()
    record_.phonenumber = self.request.get('phonenumber')
    record_.email = self.request.get('email')
    record_.description = self.request.get('description')
    record_.put()  #saving 
    return " [[Record has been Updated to]] <br/>~~~~~~~~~~<br/> " + phonebook_form.static_form_(self, record_key)
  return " [[No Record Updated as no Record has been provided]]"
  
def update_list_(self):
  return phonebook_form.static_list_(self, "update")
  