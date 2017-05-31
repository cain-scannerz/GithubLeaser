import pycurl
import urllib2
from StringIO import StringIO
from io import BytesIO
import json
import string
import os

storage = StringIO()
buffer = BytesIO()
c = pycurl.Curl()

try:
	# Do the initial call to get the latest release
	c.setopt(c.URL, 'https://api.github.com/repos/fluid-player/fluid-player/releases/latest')
	c.setopt(c.HTTPHEADER, ['Accept: application/json', 'Authorization: token b69e4c761d334864afac0c0acf064a41ef0410ed'])
	c.setopt(c.WRITEFUNCTION, storage.write)
	c.perform()
	c.close()
	data  = json.loads(storage.getvalue())

	# Check to see if we already have a folder for that release
	# If not create and download the latest version
	tarball = data['tarball_url']
	print tarball
	versionList = string.split(tarball, '/v')
	finalVerion = versionList[-1]
	if (os.path.isdir("current/web/" + finalVerion)):
		print "Version found. Exiting..."
		quit()
	else:
		c1 = pycurl.Curl()
		c1.setopt(c1.URL, tarball)
		c1.setopt(c1.HTTPHEADER, ['Accept: application/json', 'Authorization: token b69e4c761d334864afac0c0acf064a41ef0410ed'])
		c1.setopt(c1.WRITEFUNCTION, buffer)
		c1.perform()
		c1.close()
	
except pycurl.error, error:
    errno, errstr = error
    print 'An error occurred: ', errstr
