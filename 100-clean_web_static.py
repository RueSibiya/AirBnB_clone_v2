#!/usr/bin/env python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean.
"""
from fabric.api import env, local, run
from os.path import exists
from datetime import datetime

env.hosts = ['<54.237.49.126>', '<54.87.207.255>']
env.user = 'kathy2470'  # Update with your username
env.key_filename = '/home/kathy2470/.ssh/id_rsa'


def do_clean(number=0):
    """Deletes out-of-date archives."""
    try:
        number = int(number)
        if number < 1:
            number = 1
        number += 1
        with cd('/data/web_static/releases'):
            run('ls -t | grep web_static | tail -n +{} | xargs rm -rf'.format(number))
        with lcd('versions'):
            local('ls -t | grep web_static | tail -n +{} | xargs rm -rf'.format(number))
    except ValueError:
        pass
