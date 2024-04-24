#!/bin/python3
'''Creates a gddzip archive'''
from fabric.api import *
from datetime import datetime
import os


@task
def do_pack():
    '''
    produces a tgz file from args passed
    args
    '''
    date = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    filename = f'web_static_{date}.tgz'
    if not os.path.exists('./versions'):
        os.mkdir('./versions')
    if local(f'tar -zcvf versions/{filename} web_flask').succeeded:
        print("compression completd")
        path = '{}/versions/{}'.format(os.getcwd(), filename)
        return (path)
    else:
        return None
