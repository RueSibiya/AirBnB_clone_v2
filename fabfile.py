#!/usr/bin/python3
"""
This script automates the deployment of web_static using Fabric.
"""

from fabric.api import env, run, put

env.hosts = [54.237.49.126]  # Update with your server IP
env.user = 'ubuntu'  # Update with your SSH username
env.key_filename = '/home/kathy2470/.ssh/id_rsa'  # Update with your private key path


def deploy():
    """
    Deploy web_static to the server.
    """
    # Create necessary directories
    run('mkdir -p /data/web_static/releases/')
    run('mkdir -p /data/web_static/shared/')

    # Upload the latest version of web_static
    local_path = './web_static'  # Update with your local path to web_static
    remote_path = '/data/web_static/releases/'
    put(local_path, remote_path)

    # Create symbolic link
    current_release = run('ls -t /data/web_static/releases/ | head -n 1').strip()
    run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'.format(current_release))

    # Set ownership and permissions
    run('chown -R ubuntu:ubuntu /data/')
    run('chmod -R 755 /data/')
