
Pre-Install Requirements
========================
Pip has to be installed

$ apt-get install python-pip

Upgrade setuptools (>= 0.7)

$ pip install --upgrade setuptools

$ pip install requests

$ apt-get install python2.7-dev python-imaging mysql-server python-mysqldb

How to use it?
==============

1. Check it out from Github
    
    $ git clone https://github.com/zenith0/muecke-buildout-development.git

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
    
9. Browse to Shop

    http://localhost:8000
    
