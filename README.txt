What is it?
===========

This is the development buildout script for LFS. 

It will create a complete developement evironment for LFS. 

LFS is an online shop based on Python, Django and jQuery.

How to use it?
==============

1. Check it out from bitbucket
    
    $ hg clone https://bitbucket.org/diefenbach/muecke-buildout-development

2. Change to the directory

    $ cd muecke-buildout-development
    
3. Bootstrap buildout

    $ python bootstrap.py
    
4. Run buildout

    $ bin/buildout -v
    
5. Enter your database settings into muecke_project/settings.py

6. Sync your database

    $ bin/django syncdb
    
7. Initialize LFS

    $ bin/django muecke_init

8. Start server

    $ bin/django runserver
    
9. Browse to LFS

    http://localhost:8000
    
More Information
================

* `Official page <http://www.getmuecke.com/>`_
* `Documentation on PyPI <http://packages.python.org/django-muecke/index.html>`_
* `Releases on PyPI <http://pypi.python.org/pypi/django-muecke>`_
* `Source code on bitbucket.org <http://bitbucket.org/diefenbach/django-muecke>`_
* `Google Group <http://groups.google.com/group/django-muecke>`_
* `mueckeproject on Twitter <http://twitter.com/mueckeproject>`_
* `IRC <irc://irc.freenode.net/django-muecke>`_