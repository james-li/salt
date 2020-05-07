# Build package for cloudbility
## Linux:
python 2.7 is required  
### make install by virtualenv
```
#pip install virtualenv
#virtualenv /opt/salt
#. /opt/salt/bin/activate
#pip install pyzmq PyYAML pycrypto msgpack-python jinja2 psutil futures tornado
#pip install .
#rm -f /opt/salt/bin/*
#cp scripts/salt-local /opt/salt/bin/
#cp scripts/saltlocal.py /opt/salt/bin
```
# run test
login again
```
#/opt/salt/bin/salt-local --grains
```

#make package
```
#find /opt/salt -name \*.pyc -exec rm -f {} \;
#cd /opt/
#tar cvzf salt.tgz salt
```


