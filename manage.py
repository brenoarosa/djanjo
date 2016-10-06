#!/usr/bin/env python
import os
import sys

_SETTINGS = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siteconfig.settings")

if __name__ == "__main__":

    # Work around Mac OS X Lion locale misconfiguration
    curr_locale = os.environ.get('LC_CTYPE','UTF-8')
    if curr_locale == 'UTF-8':
        os.environ['LC_CTYPE'] = 'en_US.UTF-8'

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
