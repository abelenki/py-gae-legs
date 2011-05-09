#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# index_html : it's py-gae-legs' default created index html py file
##

from phonebook_datastore import Phonebook
from . import phonebook_form

#import phonebook_datastore as dstore
  
def delete_(self):
  try:
    requested_res = self.request.path_qs
    record_key = requested_res.split("/")[-1]
    if(record_key):
      record_= Phonebook.get(record_key)
      ret_val = phonebook_form.static_form_(self, record_key)
    ret_status = (" [[Record has been Deleted]]" if (record_.delete()==None) else " [[Failure Deleting Record]]" ) + " <br/>~~~~~~~~~~<br/> "
    ret_val = ret_status + ret_val
  except Exception:
    ret_val = "<div>Failure: Deletion of record has failed.</div>"
  return ret_val
  
def delete_list_(self):
  return phonebook_form.static_list_(self, "delete")
  