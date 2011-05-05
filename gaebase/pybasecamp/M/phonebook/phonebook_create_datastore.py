#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# index_html : it's py-gae-legs' default created index html py file
##

from phonebook_datastore import Phonebook

import datetime

#import phonebook_datastore as dstore

def form_(self,record_):
  ret_val =  """<form action="/phonebook/M/create" method="post">
                    <table>
		      <tr><td>Id:</td><td><input name="id" id="id" type="text" value='""" + (str(record_.id_) if (record_) else 'a number') + """' onfocus="this.value=''"></text></td></tr>
		      <tr><td>Name:</td><td><input name="name" id="name" type="text" value='""" + (str(record_.id_) if (record_) else 'full name/handle') + """' onfocus="this.value=''"></text></td></tr>
		      <tr><td>Phone#:</td><td><input name="phonenumber" id="phonenumber" type="text" value='""" + (str(record_.id_) if (record_) else 'Telephone#') + """' onfocus="this.value=''"></text></td></tr>
		      <tr><td>Email#:</td><td><input name="email" id="email" type="text" value='""" + (str(record_.id_) if (record_) else 'e@mail.id') + """' onfocus="this.value=''"></text></td></tr>
		      <tr><td>Description:</td><td><textarea name="description" id="description" rows="3" cols="60" onclick="this.value=''">'""" + (str(record_.id_) if (record_) else 'anything more') + """'</textarea></td></tr>
		    </table>
	        <div>
		      <input type="submit" value="Add Contact">
		    </div>
	      </form>"""
  return ret_val
  
  
def create_(self):
  #return str(self.request)
  new = Phonebook(id_ =int(self.request.get('id')),  name =str(self.request.get('name')))
  new.timestamp_ = datetime.datetime.now()
  new.phonenumber = self.request.get('phonenumber')
  new.email = self.request.get('email')
  new.description = self.request.get('description')
  new.put()  #saving 
  return " [[New Record]] <br/> added for <br/> " + new.name
  
