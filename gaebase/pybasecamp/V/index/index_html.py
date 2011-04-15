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
	  <title>py-gae-legs</title>
	</head>
	<body>
	  <div style="text-align:center;">
		  <div style="font-size:27px;">py-gae-legs</div>
		  <div>
		    <a href="https://github.com/abhishekkr/py-gae-legs">py-gae-legs repo @ github</a>
		  </div><br/>
		  <div>
			<span style="font-weight:bold;">py-gae-legs</span> have been initiated<br/>
		    <img src="/images/py-gae-legs-logo.jpg" alt="py-gae-legs not available"/>
		  </div><br/>
		  <div>
		    get ready to walk on Python developer legs<br/>
		    in the grounds of Gogle AppEngine<br/>
		    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>
		    it's a small project for python developers to use Google AppEngine...<br/>
		    not an effective spoon-feeder as Rails<br/>
		    but would enable you to quickly walk on your Legs<br/>
		    in the feature rich ground of GAE<br/>
		    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>
		    it's just an initial release...<br/>
		    slowly more web productivity and all the features from GAE<br/>
		    will get added to it<br/>
		    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>
		    AbhishekKr ~ ABK ~ aBionic<br/>
		    <a href="http://www.twitter.com/aBionic">http://www.twitter.com/aBionic</a><br/>
		    <a href="http://github.com/abhishekkr">http://github.com/abhishekkr</a><br/>
		    <a href="http://abhishekkr.wordpress.com">http://abhishekkr.wordpress.com</a>
		  </div>
	  </div><br/><br/>
	  <div style="text-align:center;">
	    <a href="/zdebug">see if debug page is working</a>
	  </div>
	</body>
  </html>"""