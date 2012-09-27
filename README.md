aptfax-webpy
============

This is just a demo of the webpy-mongodb technology stack

Setup
=====
<table>
  <tr>
    <td>Python 2.7</td><td>Download and install binaries from http://www.python.org/download/releases/2.7/</td>
  </tr>
  <tr>
	<td>MongoDB</td><td>Download and install binaries from http://www.mongodb.org/downloads</td>
  </tr>
  <tr>
	<td>webpy</td><td>easy_install webpy or download from http://webpy.org/download</td>
  </tr>
  <tr>
	<td>pymongo</td><td>easy_install pymongo or download from http://pypi.python.org/pypi/pymongo/</td>
  </tr>
  <tr>
	<td>aptfax</td><td>Clone this repository into local machine</td>
  </tr>
</table>

Running
=======
* Run mongod

``` path/to/mongodb/bin > mongod ```

* Run aptfax

``` path/to/aptfax/ > python application.py ```

Once you have this running, you should be able to access the application at http://localhost:8080/posts using your web browser.