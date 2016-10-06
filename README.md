# Robust django template

### Setting up environment

~~~~
mkvirtualenv [venv-name] -p python3
pip install pip --upgrade
pip install -r requirements.txt
~~~~

[**Working with virtualenvs**](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

### Django Configs

A custom setting system based on http://justcramer.com/2011/01/13/settings-in-django/  
This enable us to easily maintain multiple environments (e.g.: dev, stage, production, etc)

All configurations will be loaded from siteconfig/{env}.py and heavely inheriting from siteconfig/defaults.py

### Starting project

- Rename project name (currently: 'compass') to the choosed one.  
Little help:
~~~~
find . -name '*compass*'  | grep compass && grep 'compass' -riI . --exclude-dir=.git
~~~~

- Review configurations

- Start working!
