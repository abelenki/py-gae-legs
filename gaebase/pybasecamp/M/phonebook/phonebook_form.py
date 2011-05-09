#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# phonebook_form : it's py-gae-legs' default created phonebook input-form py file
##

from google.appengine.ext import db
from phonebook_datastore import Phonebook

def form_(self, record_key, action_):
  record_=""
  if(action_!="create"):
    record_=Phonebook.get(record_key)
  ret_val =  """<form action='/phonebook/M/""" + ((action_ + "/" + str(record_.key())) if (record_) else action_) +"""' method="post">
                    <table>
		      <tr><td>Name:</td><td><input name="name" id="name" type="text" value='""" + (str(record_.name) if (record_) else 'full name/handle') + """' onfocus="this.value=''"></text></td></tr>
		      <tr><td>Phone#:</td><td><input name="phonenumber" id="phonenumber" type="text" value='""" + (str(record_.phonenumber) if (record_) else 'Telephone#') + """' onfocus="this.value=''"></text></td></tr>
		      <tr><td>Email#:</td><td><input name="email" id="email" type="text" value='""" + (str(record_.email) if (record_) else 'e@mail.id') + """' onfocus="this.value=''"></text></td></tr>
		      <tr><td>Description:</td><td><textarea name="description" id="description" rows="3" cols="60" onclick="this.value=''">""" + (str(record_.description) if (record_) else 'anything more') + """</textarea></td></tr>
		    </table>
	        <div>
		      <input type="submit" value=\"'""" + action_ +"""\' Contact">
		    </div>
      </form>"""
  return ret_val

def static_form_(self, record_key):
  record_=""
  if(record_key):
    record_=Phonebook.get(record_key)
    ret_val =  """<div>
                    <table>
		      <tr><td>Name:</td><td><label name="name" id="name">""" + (str(record_.name) if (record_) else 'full name/handle') + """</label></td></tr>
		      <tr><td>Phone#:</td><td><label name="phonenumber" id="phonenumber">""" + (str(record_.phonenumber) if (record_) else 'Telephone#') + """</label></td></tr>
		      <tr><td>Email#:</td><td><label name="email" id="email">""" + (str(record_.email) if (record_) else 'e@mail.id') + """</label></td></tr>
		      <tr><td>Description:</td><td><label name="description" id="description">""" + (str(record_.description) if (record_) else 'anything more') + """</label></td></tr>
		    </table>
		    </div>"""
    return ret_val
  return "No Record Provided"
  
#entire list
def static_list_(self, action_):
  datab_ = db.GqlQuery("SELECT * FROM Phonebook")
  ret_val = "<div><table><tr>"
  ret_val = ret_val + "<td>id#</td>"
  ret_val = ret_val + "<td>Name</td>"
  ret_val = ret_val + "<td>Phonenumber</td>"
  ret_val = ret_val + "<td>Email</td>"
  ret_val = ret_val + "<td>Description</td>"
  ret_val = ret_val + "<td>Timestamp_</td>"
  ret_val = ret_val + "<td></td>"
  ret_val = ret_val + "</tr>"
  for record_ in datab_:
    ret_val = ret_val + "<tr>"
    ret_val = ret_val + "<td>" + str(record_.key().id()) + "</td>"
    ret_val = ret_val + "<td>" + str(record_.name) + "</td>"
    ret_val = ret_val + "<td>" + str(record_.phonenumber) + "</td>"
    ret_val = ret_val + "<td>" + str(record_.email) + "</td>"
    ret_val = ret_val + "<td>" + str(record_.description) + "</td>"
    ret_val = ret_val + "<td>" + str(record_.timestamp_) + "</td>"
    ret_val = ret_val + "<td><a id=\"update\" href=\"/phonebook/V/" + (action_ if(action_) else "read") + "/" + str(record_.key()) + "\">"
    ret_val = ret_val + "[" + (action_ if(action_) else "read") + "]</a></td>"
    ret_val = ret_val + "<tr>"
  ret_val = ret_val + "</table></div>"
  return ret_val
  