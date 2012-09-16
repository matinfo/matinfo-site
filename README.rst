
#######################################
Personal site based on Django framework
#######################################

This is a good example including good practice of a personal Web site with Django & Zinnia blog using djangoprojectrecipe. 
Include a setup made with buildout, the server run gunicorn, ngnix and supervisor.

Summary
#######

* Django > 1.4.0 
* Zinnia > 1.11 perfect Django blog 
* HTML5 templates
* Custom template for a single blog interface - one column / no sidebar

Setup your local settings (dev)
###############################

* A $ copy 'personal.cfg-dist' file to 'personal.cfg' (addapt it if necessary).

* B $ copy 'py_src/project/settings/personal.py-dist' to 'py_src/project/settings/personal.py' and make necessary change, like DB connection.

Start runnning it locally (dev)
###############################

Run the following commands::

    ./init.sh -c personal.cfg
    bin/django syncdb
    bin/django migrate
    bin/django runserver

Done
