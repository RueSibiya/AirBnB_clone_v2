#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from contents of web_static
folder of your AirBnB Clone repo
"""
from fabric.api import task
from datetime import datetime

env.hosts = ['54.237.49.126']

@task
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder

    Returns:
        str: Path of the generated archive if successful, None otherwise
    """
    try:
        # Create the folder versions if it doesn't exist
        local("mkdir -p versions")

        # Generate the name of the archive using the current timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)

        # Create the .tgz archive using tar
        local("tar -cvzf {} web_static".format(archive_name))

        # Return the path of the archive if it's generated successfully
        return archive_name
    except Exception as e:
        return None
