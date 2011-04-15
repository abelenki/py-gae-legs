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
        <div style="font-size:27px;">Create</div>
		<div>
		  <span style="font-weight:bold;">PhoneBook</span>
		</div><br/>
		<div>
          <form action="/M/phonebook/create" method="post">
            <div>
		      Name:<input name="name" id="name" type="text"></text><br/>
		      Phone#:<input name="phonenumber" id="phonenumber" type="text"></text><br/>
		      Description:<textarea name="description" id="description" rows="3" cols="60"></textarea>
		    </div>
	        <div>
		      <input type="submit" value="Add Contact">
		    </div>
	      </form>
		</div>
	  </div><br/><br/>
	  <div style="text-align:center;">
	    <a href="/">Homepage</a>
	  </div>
	</body>
  </html>"""