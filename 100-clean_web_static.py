#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives.
"""

from fabric.api import *
from fabric.contrib import files
import os

env.hosts = ['34.207.58.40', '54.237.58.210']

def do_clean(number=0):
    number = int(number)
    if number == 0:
        number = 1

    # Clean local archives
    local_archives = sorted(os.listdir("versions"))
    [local("rm versions/" + file) for file in local_archives[:-number]]

    # Clean remote archives
    with cd('/data/web_static/releases'):
        remote_archives = run('ls -tr').split()
        archives_to_keep = remote_archives[-number:]
        archives_to_delete = [file for file in remote_archives if file not in archives_to_keep]

        # Ensure to not delete if we have directories that don't match the archive naming convention
        valid_archives_to_delete = [file for file in archives_to_delete if "web_static_" in file]

        for file in valid_archives_to_delete:
            run('rm -rf ./{}'.format(file))

