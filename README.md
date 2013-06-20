+++++++++++++++++++
python-HTMLEntity
+++++++++++++++++++

HTML Entities for Python

Installing
==========

For install python-HTMLEntity, run on terminal: ::

    $ git clone git@github.com:wangjingbupt/python-HTMLEntity.git
    $ cd python-HTMLEntity
		$ [sudo] python setup.py install

Using python-HTMLEntity
==================

encoding
--------

Normal encode ::

    import htmlentities

    htmlentities.encode('<') # returns "&lt"

Deal with Chinese or other Special character, please use unicode string ::

    import htmlentities
		
		t = '测试'.decode('utf-8') // '测试'.decode('gbk')

		htmlentities.encode(t) # returns ""

decoding
--------

    import htmlentities

    htmlentities.decode('&lt') # returns "<"
    
		htmlentities.decode('&lt') # returns ""


