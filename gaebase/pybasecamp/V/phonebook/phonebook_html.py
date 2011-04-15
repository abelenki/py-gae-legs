#!/usr/bin/env python
##
# https://github.com/abhishekkr/py-gae-legs
#
# index_html : it's py-gae-legs' default created index html py file
##

def get_headers(self):
  headers={"Content-Type":"text/html"}
  return headers 

def get_html(self):
  return """<html>
    <head>
	  <title>py-gae-legs ~ PhoneBook</title>
	</head>
	<body>
	  <div style="text-align:center;">
		  <div style="font-size:27px;">PhoneBook</div>
		  <div>
			<span style="font-weight:bold;">CRUD Pages</span>
		  </div><br/>
		  <div>
		    <a href="/V/phonebook/create">Create 'PhoneBook' Entry</a><br/>
		    <a href="/V/phonebook/read">Read Entire 'PhoneBook'</a><br/>
		    <a href="/V/phonebook/update">Update 'PhoneBook' Entry</a>
		    <a href="/V/phonebook/delete">Delete 'PhoneBook' Entry</a>
		  </div>
	  </div><br/><br/>
	  <div style="text-align:center;">
	    <a href="/">Homepage</a>
	  </div>
	</body>
  </html>"""