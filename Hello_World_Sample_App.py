#printing hello world
my_name = "sandeep"




print("Hello world and welcome " + my_name + "!")
import logging
#set log level
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler('hello_world_app_logs.log')
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

#log messages 
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical messge')

#printing the helloworld environment variable
import os
 
#print(os.environ)

#set environment variabl
os.environ['HELLO_WORLD'] = 'Hello World'

#get environment variable 
ENV_VAR = os.getenv('HELLO_WORLD')

print(ENV_VAR)

#set the environment variable using ansible 






