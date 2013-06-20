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

encode
--------

Normal encode ::

import HTMLEntity

HTMLEntity.encode('<') # returns '&lt'

Deal with Chinese or other Special character, please use unicode string ::

import HTMLEntity
		
t = '测试'.decode('utf-8') # '测试'.decode('gbk')

HTMLEntity.encode(t) # returns '&#27979;&#35797;'

decode
--------
import HTMLEntity

HTMLEntity.decode('&lt') # returns '<'
    
HTMLEntity.decode('&#27979;&#35797;') # returns '测试'

HTMLEntity.decode('&#x5b9e;&#x4f53;&#x5b57;&#x7b26;') # returns '实体字符'

Thanks
===========
	This work is depend on https://github.com/cobrateam/python-htmlentities

About 
===========

  contact: wangjingbupt@gmail.com
