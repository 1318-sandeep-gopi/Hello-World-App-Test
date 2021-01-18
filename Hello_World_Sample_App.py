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

#Set environment variables
os.environ['HELLO_WORLD'] = 'Sandeep'

#get environment variable 
USER = os.getenv('HELLO_WORLD')

print(USER)






