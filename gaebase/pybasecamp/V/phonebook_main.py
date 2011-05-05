#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# index_html : it's py-gae-legs' default created index html py file
##

from ..M.phonebook import phonebook_create_datastore
from ..M.phonebook import phonebook_read_datastore

def _form_datastore(self):
    return phonebook_create_datastore.form_(self,"")

def _create_datastore(self):
    return phonebook_create_datastore.create_(self)
    
def _read_datastore(self):
    return phonebook_read_datastore.read_(self)
  
#####end=of=phonebook_html