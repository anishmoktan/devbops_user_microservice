#!/usr/bin/python3
import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/devbops_user_microservice/")

def application(environ, start_response):
    for key in ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY']: #loads AWS credentials for containers' environmental variables to use
        os.environ[key] = environ.get(key, '') #we need to create our own env file

    from devbops_user_microservice import app as application
    return application(environ, start_response)
