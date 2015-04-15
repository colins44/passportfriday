# -*- mode: ruby -*-
# vi: set ft=ruby :

# specify different environments: dev, uat, stage, prod
BUILD_ENVIRONMENT = ENV["OST_ENV"] || "dev"

Vagrant.configure("2") do |config|
    config.ssh.forward_agent = true
    config.vm.box = "ubuntu/trusty64"

    # custom configurations for different environments
    case BUILD_ENVIRONMENT
        when "uat"
            config.vm.network :public_network, type: "dhcp"
        when "stage"
            config.vm.provider "aws"
    end

    # run provisioner, based on environment
    # TODO: replace scripts with proper Puppet recipes
    config.vm.provision "shell", path: "conf/#{BUILD_ENVIRONMENT}/provision.sh"

end

#art for passport fridays
#AWS elastic Beanstalk, scales, builds and pushes the new images to all the EC2 images
#amazon EC2 running linux
#amazon RDS running the postgres database
#amazon S3 hosting the static files, CSS, JS, IMAGES
#look into database caching??????
#what about running tasks on a seperate server? Asyncronus tasks with SQS (Amazon version of celery?)
#Move away from docker to vagrant ?
#store user sessions on dynimo DB

