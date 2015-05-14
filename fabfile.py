import os
from fabric.api import *
from fabric.colors import green, red, cyan
from fabric.contrib.files import exists
from fabric import context_managers
import boto.ec2


PASSPORTFRIDAYS_AWS_ACCESS_KEY_ID = ''
PASSPORTFRIDAYS_AWS_SECRET_ACCESS_KEY = ''
PASSPORTFRIDAYS_INSTANCE = 'i-dc7a463a'
env.use_ssh_config = True

@task
def vagrant():
    env.user = 'vagrant'
    key_result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.remote_app_dir = '/vagrant'
    env.virtual_env_dir = '/usr/local/venv/sky'
    env.key_filename = key_result.split()[1]
    port_result = local('vagrant ssh-config | grep Port', capture=True)
    env.hosts = ['127.0.0.1:%s' % port_result.split()[1]]
    env.machine_name = 'vagrant'

@task
def staging():
    """ Set the target to Staging. """
    #change this line to look up IP address on DO or AWS
    env.elastic_ip = get_ip_address('ami image eg:i-bf17111a')
    #if deplying on ubuntu keep otherwise change to linux etc
    env.hosts = ['ubuntu@%s' % (env.elastic_ip,)]
    env.key_filename = '~/.ssh/passportfridays.pem'
    #where should the project go???
    env.remote_app_dir = '/usr/local/src/passportfirdays'
    #are we installing a virtualenv, maybe, maybe not as its a dedicated machine
    #env.virtual_env_dir = '/home/ubuntu/.virtualenvs/passportfridays'
    env.machine_name = 'staging'

@task
def launch_instance(self):
    """Launches an EC2 instance"""
    conn = boto.ec2.connect_to_region(
        "eu-west-1",
        #aws_access_key_id=os.environ.get('PASSPORTFRIDAYS_AWS_ACCESS_KEY_ID'),
        aws_access_key_id=PASSPORTFRIDAYS_AWS_ACCESS_KEY_ID,
        #aws_secret_access_key=os.environ.get('PASSPORTFRIDAYS_AWS_SECRET_ACCESS_KEY')
        aws_secret_access_key=PASSPORTFRIDAYS_AWS_SECRET_ACCESS_KEY
    )
    conn.run_instances(
        'ami-5da23a2a',
        instance_type='t1.micro',
        security_groups=["passportfridays"])

@task
def get_ip_address(instance_id):
    #aws_access_key_id=os.environ.get('PASSPORTFRIDAYS_AWS_ACCESS_KEY_ID')
    #aws_secret_access_key=os.environ.get('PASSPORTFRIDAYS_AWS_SECRET_ACCESS_KEY')
    aws_access_key_id = PASSPORTFRIDAYS_AWS_ACCESS_KEY_ID
    aws_secret_access_key = PASSPORTFRIDAYS_AWS_SECRET_ACCESS_KEY
    if aws_access_key_id is None or aws_secret_access_key is None:
        print(red('Your need to set your environment variables for AWS.'))
    else:
        conn = boto.ec2.connect_to_region("eu-west-1", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        box = conn.get_all_reservations(instance_ids=[instance_id])
        print(red('Found this amazon box: %s - ip: %s' % (box[0].instances[0].tags['Name'],box[0].instances[0].ip_address,)))
        return box[0].instances[0].ip_address

@task
def hello():
    print 'colin'

@task
def prepare_deploy():
    local("python /vagrant/manage.py test")

@task
def provision():
    run('sudo apt-get update')
    run('sudo apt-get upgrade')
    run('sudo apt-get install libpq-dev python-dev nginx python-pip git python-setuptools memcached supervisor postgresql')
    run('sudo pip install -r /vagrant/requirements.txt')
    run('sudo mkdir /vagrant/passportfridays/logs')

@task
def createdb():
    run('sudo su postgres')
    run('psql')
    run("CREATE DATABASE passportfridays OWNER dirtypunit ENCODING 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8' TEMPLATE template0;")

@task
def whoami():
    run('whoami')

@task
def host_type():
    run('uname -s')



