#import ctfcli
import __main__

import subprocess,os,sys
from pathlib import Path

from ctfcli.utils.utils import debuggreen,debugyellow
################################################################################
##############                   Master Values                 #################
################################################################################
# set to true to enable debugging messages in the terminal
global DEBUG
DEBUG = True

# puts this directory in the path
debugyellow(f"Inserting current folder into $PATH at index 0")
sys.path.insert(0, os.path.abspath('.'))

#Before we load the menu, we need to do some checks
# Where the terminal is located when you run the file
PWD = os.path.realpath(".")
#PWD_LIST = os.listdir(PWD)

# ohh look a global list
global PROJECT_ROOT
# this is a testing line for small snippets in bpython
# WHEN THE SHELL IS PWD == PROJECTROOT
#PROJECT_ROOT = PWD
PROJECT_ROOT = Path(os.path.dirname(__file__))
debuggreen(f"Project root located at {PROJECT_ROOT}")

# The .env needs to be reloaded in the case of other alterations
global ENVFILE
ENVFILE = Path(PROJECT_ROOT,'.env')
debuggreen(f"Env file located at {ENVFILE}")

# challenges repository
global CHALLENGEREPOROOT
CHALLENGEREPOROOT=Path(PROJECT_ROOT,'/data/CTFd')
debuggreen(f"Challenge Repository located at {CHALLENGEREPOROOT}")

# docker-compose files directory
global COMPOSEDIRECTORY
COMPOSEDIRECTORY = Path(PROJECT_ROOT,'/data/composefiles')
debuggreen(f"Docker Compose directory located at {COMPOSEDIRECTORY}")

# kubernetes configuration directory
global KUBECONFIGPATH
KUBECONFIGPATH = Path(PROJECT_ROOT, '/data/kubeconfig/')
debuggreen(f"kubectl config located at {KUBECONFIGPATH}")
