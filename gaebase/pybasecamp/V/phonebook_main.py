#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# phonebook_main : it's py-gae-legs' default created phonebook-datastore-main py file
##

#importing ML generating Py
from ..M.phonebook import phonebook_create_datastore
from ..M.phonebook import phonebook_read_datastore
from ..M.phonebook import phonebook_update_datastore
from ..M.phonebook import phonebook_delete_datastore

def _createform_datastore(self):
  return phonebook_create_datastore.create_(self)

def _create_datastore(self):
  return phonebook_create_datastore.create_list_(self)

def _readform_datastore(self):
  return phonebook_read_datastore.read_(self)
    
def _read_list_datastore(self):
  return phonebook_read_datastore.read_list_(self)

def _updateform_datastore(self):
  return phonebook_update_datastore.update_form(self)
    
def _update_datastore(self):
  return phonebook_update_datastore.update_(self)
    
def _update_list_datastore(self):
  return phonebook_update_datastore.update_list_(self)
    
def _delete_datastore(self):
  return phonebook_delete_datastore.delete_(self)
    
def _delete_list_datastore(self):
  return phonebook_delete_datastore.delete_list_(self)
    
def _delete_all_datastore(self):
  return phonebook_delete_datastore.delete_all_(self)
  
#####end=of=phonebook_html