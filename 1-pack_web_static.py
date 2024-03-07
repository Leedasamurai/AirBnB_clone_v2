#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    # Create the directory versions if it doesn't exist
    local("mkdir -p versions")

    # Generate the archive's filename
    file_name = "versions/web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))

    try:
        # Create the archive using tar command
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
