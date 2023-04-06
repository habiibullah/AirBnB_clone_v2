#!/usr/bin/python3
"""
Script generates a .tgz archive from web_static folder
"""
from fabric.operations import local, run, put, env
from datetime import datetime
import os


env.hosts = ['35.168.2.117', '54.146.9.154']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
        Distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False

    _path = archive_path.split("/")
    path_no_ext = _path[1].split(".")[0]

    try:
        put(archive_path, "/tmp")
        run("sudo mkdir -p /data/web_static/releases/" + path_no_ext + "/")
        run("sudo tar -xzf /tmp/" + path_no_ext + ".tgz" +
            " -C /data/web_static/releases/" + path_no_ext + "/")
        run("sudo rm /tmp/" + path_no_ext + ".tgz")
        run("sudo mv /data/web_static/releases/" + path_no_ext +
            "/web_static/* /data/web_static/releases/" + path_no_ext + "/")
        run("sudo rm -rf /data/web_static/releases/" +
            path_no_ext + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/" + path_no_ext +
            "/ /data/web_static/current")
        return True

    except Exception:
        return False
