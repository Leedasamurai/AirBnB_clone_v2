#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py
"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = "ubuntu"
env.key_filename = "my_ssh_private_key"

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Extract the archive filename and the filename without extension
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(file_name))

        # Create directory to uncompress the archive
        run("mkdir -p /data/web_static/releases/{}/".format(no_ext))

        # Uncompress the archive
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, no_ext))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))

        # Move the content to the correct folder and delete the directory from the archive
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(no_ext, no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))

        # Delete the current symbolic link and create a new one
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(no_ext))

        print("New version deployed!")
        return True
    except Exception as e:
        return False
