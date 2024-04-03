#!/usr/bin/env python3
from fabric import task
from os.path import exists
from fabric import Connection

env.hosts = ['<54.237.49.126>', '<54.87.207.255>']
env.user = 'kathy2470'  # Update with your username
env.key_filename = '/home/kathy2470/.ssh/id_rsa'  # Update with the path to your SSH private key

@task
def do_deploy(c, archive_path):
    """
    Distributes an archive to your web servers
    """
    if not exists(archive_path):
        print("Archive does not exist")
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        c.put(archive_path, '/tmp')

        # Extract the archive to the folder /data/web_static/releases/<archive filename without extension>
        filename = archive_path.split('/')[-1]
        folder = "/data/web_static/releases/{}".format(filename.split('.')[0])
        c.run("mkdir -p {}".format(folder))
        c.run("tar -xzf /tmp/{} -C {}".format(filename, folder))

        # Delete the archive from the web server
        c.run("rm /tmp/{}".format(filename))

        # Move the contents of the extracted folder to the parent folder
        c.run("mv {}/web_static/* {}".format(folder, folder))

        # Delete the empty web_static directory
        c.run("rm -rf {}/web_static".format(folder))

        # Remove the current symbolic link
        c.run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new version of your code
        c.run("ln -s {} /data/web_static/current".format(folder))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed:", e)
        return False
