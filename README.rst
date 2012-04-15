
#######################################
Personal site based on Django framework
#######################################

This is a good example and good practice with Django, Zinnia (blog), gunicorn, ngnix, supervisor, buildout, djangoprojectrecipe.

Summary
#######

* Django >= 1.4.0 
* Zinnia Django perfect blog 
* HTML5 oriented
* Custom template for simple blog interface (ongoing)


Init your local development settings
####################################

* A $ copy 'personal.cfg-dist' file to 'personal.cfg' (addapt it if necessary).

* B $ copy 'py_src/project/settings/personal.py-dist' to 'py_src/project/settings/personal.py' and make necessary change, like DB connection.


Start runnning it locally (dev)
###############################

Run the following commands::

    ./init.sh -c personal.cfg
    mkdir tmp
    bin/django syncdb --all
    bin/django migrate --fake
    bin/django runserver

Done
