#!/usr/bin/python3
'''Creates a gdzip archive'''
from fabric.api import *
from datetime import datetime
import os


web_01 = '100.24.235.89'
web_02 = '52.87.232.104'
lb = '100.24.72.21'
key_filename = '~/.ssh/school'
env.hosts = [web_02, web_01]
env.key_filename = key_filename
env.cwd = '~/'
env.user = 'ubuntu'


@task
def do_deploy(archive_path):
    '''distributes an archive to a server'''
    name = archive_path.split('.')[0]
    name = name.split('/')[1]
    r_cmd = f'rm -rf /tmp/{name}.tgz /data/web_static/current'
    sym = '/data/web_static/current'
    c_sym_ln = f'ln -s /data/web_static/releases/{name} {sym}'
    if os.path.exists(archive_path):
        upload = put(archive_path, '/tmp/')
        if upload.succeeded:
            new_dir = run(f'mkdir -p /data/web_static/releases/{name}')
            if new_dir.succeeded:
                with cd(f'/data/web_static/releases/{name}'):
                    command = f'tar -xzvf /tmp/{archive_path.split("/")[1]}'
                    unzip = sudo(command)
                    if unzip.succeeded:
                        '''Probably should check for errors here'''
                        sudo('mv /web_static/* ./')
                        sudo(r_cmd)
                        sudo(c_sym_ln)
                        return True
    else:
        return False
    return False
