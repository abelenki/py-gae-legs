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
  response= """<html>
    <head>
	  <title>py-gae-legs</title>
	</head>
	<body>
	  <div style="text-align:center;">
        <div style="font-size:27px;">Create</div>
		<div>
		  <span style="font-weight:bold;">PhoneBook</span>
		</div><br/>
		<div>"""
  response = response + "Name: " + name
  response = response + "Phone#" + phonenumber
  response = response + "Description" + description
  response = response + "~~~~~~~~~~~~~~~~~~~~~~~~~~~"  
  response = response + """</div>
		</div>
	  </div><br/><br/>
	  <div style="text-align:center;">
	    <a href="/">Homepage</a>
	  </div>
	</body>
  </html>"""
  return response