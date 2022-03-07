#This file is going to be the main file after start.sh I guess?

# HUGE TODO: SET PATHS CORRECTLY EVERYTHING IS BROKENNNN!!!!!
# repository managment
from ctfcli.__main__ import Ctfcli
from ctfcli.utils.utils import greenprint,errorlogger,debuggreen,debugyellow


# top scope imports
from data.utils import getenv,setenv,putenv
# info for docker pull
from data.dockerpulls import *

# basic imports
import fire
import subprocess,os,sys
from pathlib import Path
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

######################################################
##  KUBERNETES SETTINGS
######################################################

KUBECONFIG = "./data/kubeconfig"
KUBECONTEXT = "meeplabben"

def createsandbox():
    '''
    Creates the sandbox, using kubernetes/docker
    '''
    # set environment to read from kube config directory
    debugyellow("Setting Environment from .env in project root")
    getenv(ENVFILE)
    #setenv({"KUBECONFIG":KUBECONFIGPATH})

def runsandbox(composefile):
    '''
    run a sandbox

    Args:
        composefile (str): composefile to use
    '''
    subprocess.Popen(["docker-compose", "up", composefile])

################################################################################
##############      The project formerly known as sandboxy     #################
################################################################################
class Project():
    def __init__(self,projectroot:Path):
        self.root = projectroot
        self.datadirectory = Path(self.root, "data")
        self.extras = Path(self.root, "extra")
        self.containerfolder = Path(self.root, "containers")
        self.mysql = Path(self.root, "data", "mysql")
        self.redis = Path(self.root, "data", "redis")
        self.persistantdata = [self.mysql,self.redis]

    def cleantempfiles(self):
        """
        Cleans temoporary files
        """
        for directory in self.persistantdata:
            # clean mysql
            for file in os.listdir(directory):
                if os.exists(Path(os.path.abspath(file))):
                    os.remove(Path(os.path.abspath(file)))
            # clean redis
            #for file in os.listdir(self.mysql):
            #    os.remove(Path(os.path.abspath(file)))



class MenuGrouping():
    '''
        DO NOT MOVE THIS FILE \n
    This is the main menu of the project, \n
    Project.__init__ is where you explicitly define the paths \n
    of the folders expected \n\n
    
    This class is where you build the menu calling other actions

    '''
    def __init__(self):
        # challenge templates
        self.name = "lol"
        self.project_actions = Project(PROJECT_ROOT)
        self.injectENV = getenv(ENVFILE)
        self.cli = Ctfcli()

def main():
   fire.Fire(MenuGrouping)

if __name__ == "__main__":
    main()
    #fire.Fire(Ctfcli)

