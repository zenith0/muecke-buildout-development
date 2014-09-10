WebShop
=======

How to install?
--------------
Check it out from GitHub

$ git clone git@github.com:zenith0/muecke.git

Change to the directory

$ cd muecke

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
