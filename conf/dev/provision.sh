#! /bin/bash

# TODO: all generic packages need to go into the base vagrant box;
#       here we need only packages that are specific to this environment

wget -qO - https://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
echo "deb http://packages.elasticsearch.org/elasticsearch/1.4/debian stable main"  >> /etc/apt/sources.list

apt-get -y update
apt-get -y install postgresql libpq-dev python-dev python-pip git \
   memcached libmemcached-dev default-jre elasticsearch libjpeg-dev

# environment specific packages
apt-get -y install ack-grep python-pygraphviz

update-rc.d elasticsearch defaults 95 10
/etc/init.d/elasticsearch start

ssh-keyscan github.com > /etc/ssh/ssh_known_hosts

# TODO: check if the default username and database already exist
#       so we can re-run provision repeatedly
sudo -u postgres createuser -d vagrant || true
sudo -u postgres createdb passportfridays || true

cd /vagrant

easy_install -U pip # we need a newer version of pip than provided by Ubuntu; this should be specified by the box setup
pip install -r `pwd`/requirements.txt # install passport fridays and its dependencies
pip install -r `pwd`/conf/dev/requirements.txt # install environment-specific Python packages

# set up environment variables


# prepare testing environment
#ln -sf `pwd`/conf/dev/test_settings.py `pwd`/skylark/settings.py
