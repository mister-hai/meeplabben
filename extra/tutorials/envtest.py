import subprocess,os,sys
from pathlib import Path
################################################################################
##############                   Master Values                 #################
################################################################################
# set to true to enable debugging messages in the terminal
global DEBUG
DEBUG = True

# puts this directory in the path
sys.path.insert(0, os.path.abspath('.'))

#Before we load the menu, we need to do some checks
# Where the terminal is located when you run the file
PWD = os.path.realpath(".")
#PWD_LIST = os.listdir(PWD)

# ohh look a global list
global PROJECT_ROOT
# this is a testing line for small snippets in bpython
# WHEN THE SHELL IS PWD = PROJECTROOT
PROJECT_ROOT = PWD
#PROJECT_ROOT = Path(os.path.dirname(__file__))

# The .env needs to be reloaded in the case of other alterations
global ENVFILE
ENVFILE = Path(PROJECT_ROOT,'.env')

global CHALLENGEREPOROOT
CHALLENGEREPOROOT=Path(PROJECT_ROOT,'/data/CTFd')

global COMPOSEDIRECTORY
COMPOSEDIRECTORY = Path(PROJECT_ROOT,'/data/composefiles')

global KUBECONFIGPATH
KUBECONFIGPATH = Path(PROJECT_ROOT, '/data/kubeconfig/')

bash_script = f'''#!/usr/bin/env bash
set -a
source {ENVFILE}
set +a
'''

def getenv(envfile):
    """
    reads the .env file for the project
    you must specify the full path to the .env file

    .env is in PROJECTROOT
    """
    # ugly hack because dotenv doesnt install?
    # sources the given .env 
    bash_script = f'''#!/usr/bin/env bash
set -a
source {envfile}
set +a
'''
    cmd = subprocess.Popen(bash_script,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, error = cmd.communicate()
    for output_line in output.decode().split('\n'):
        print(output_line)
    #for error_lines in error.decode().split('\n'):
    #    critical_message(error_lines)

print("ENV file located at:")
print(ENVFILE)
print("sourcing envfile with the following script")
print("==============================\n\n"+bash_script+"\n\n==============================")
getenv(ENVFILE)
for each in os.environ:
    print(each)