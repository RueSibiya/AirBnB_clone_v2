#!/usr/bin/env python3
"""Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers using the function deploy."""

from fabric.api import env, local, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['<54.237.49.126>', '<54.87.207.255>']  # Update with your server IP


def do_pack():
    """Create a .tgz archive of the web_static folder."""
    try:
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Distribute an archive to your web servers."""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        folder_name = archive_name.split('.')[0]
        remote_path = "/data/web_static/releases/{}/".format(folder_name)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(remote_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, remote_path))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}web_static/* {}".format(remote_path, remote_path))
        run("rm -rf {}web_static".format(remote_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(remote_path))

        return True
    except Exception as e:
        return False


def deploy():
    """Create and distribute an archive to your web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
