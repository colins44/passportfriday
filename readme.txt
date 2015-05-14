#TODO update this

this django project runs within a Vagrant box using a Postgres DB, dont follow the steps below so closely

steps:

1. run:
    $ vagrant up

2. ssh into the Vagrant box:
    $ vagrant ssh

3. update the system:
    $ sudo apt-get update

4. Install required items:
    $ sudo apt-get install libpq-dev python-dev nginx python-pip git python-setuptools memcached supervisor postgresql

5. Install required python packages:
    $ sudo pip install -r /vagrant/requirements.txt
    $ sudo mkdir /vagrant/passportfridays/logs

6. Make the Postgres DB:
    $ sudo su postgres
    % create user dirtypunit -P (now follow prompts, select N for all)
    $ psql
    within psql rin this line:  CREATE DATABASE passportfridays OWNER dirtypunit ENCODING 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8' TEMPLATE template0;
    then exit postgres with: \q
    then to exit postgres: $ exit
    you should be back in vagrant now with a postgres DB

7. Run the Migrations, create user, load fixtures and start dev server:
    $ cd /vagrant
    $ ./manage.py migrate
    $ ./manage.py createsuperuser (follow instructions)
    $ ./manage.py loaddata > flights/fixtures/dates.yaml
    $ ./manage.py loaddata > flights/fixtures/flights.yaml
    $ ./manage.py loaddata > flights/fixtures/location.yaml
    $ ./manage.py runserver 0.0.0.0:8000

8. Navigate to the following addresses:
    http://localhost:8080/   --for homepage
    http://localhost:8080/admin  --to login with your new username and passport



