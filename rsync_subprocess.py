import os
import urllib.request
import json
import platform
import subprocess
import sys
from fabric import Connection

def checkout(host, directory, tag):

    result = Connection(host).run('cd ' + directory + ' && git checkout ' + tag + ' && git describe > HEAD', hide=True)

    if result:

        return True

    else:

        return False

host = "opsuser@10.44.0.52"
directory = "/var/www/BHT-Core"

if checkout(host, directory, 'v4.7.8'):
    print("Successfully checked out core to v4.7.8")
else:
    print("Failed to check out Core")