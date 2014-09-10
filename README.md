WebShop
=======

Precondition
------------
Pip has to be installed

$ apt-get install python-pip

Upgrade setuptools (>= 0.7)

$ pip install --upgrade setuptools

$ apt-get install python2.7-dev python-imaging mysql-server python-mysqldb


How to install?
--------------
Check it out from GitHub

$ git clone git@github.com:zenith0/muecke.git

Change to the directory

$ cd muecke
$mkdir dlcache


Bootstrap buildout

$ python bootstrap.py

Run buildout

$ bin/buildout -v

Enter your database settings into muecke_project/settings.py

Sync your database

$ bin/django syncdb

Initialize Muecke

$ bin/django lfs_init

Start server

$ bin/django runserver

Browse to Muecke

http://localhost:8000
