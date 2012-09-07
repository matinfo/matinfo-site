#!/bin/sh
mkdir -p tmp
echo "getting boostrap.py"
if [ -f "bootstrap.py" ]; then
    rm bootstrap.py
fi
curl http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py > bootstrap.py
echo "running bootstrap.py"
python bootstrap.py
echo "running buildout"
bin/buildout $*
echo "done"