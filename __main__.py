# repository managment
from ctfcli.__main__ import Ctfcli

# info for docker pull
from data.dockerpulls import *

# basic imports
import fire
from pathlib import Path
from sys import path
from os import remove,listdir
from os.path import realpath,abspath,exists,abspath

# load utilities
from data.utils import getenv
# import global vars
from data.globals import debugyellow
import data.globals as globals

################################################################################
##############                   Master Values                 #################
################################################################################

# puts this directory in the path
debugyellow(f"Inserting current folder into $PATH at index 0")
path.insert(0, abspath('.'))

####################
### Before we load the menu, we need to do some checks
##############

# Where the terminal is located when you run the file
PWD = realpath(".")
#PWD = realpath(__file__)

# now we init the globals
# enable debugging mode
globals.debug(True)
#init paths
globals.paths(PWD)

# now load the environment variables into the module
debugyellow("Setting Environment from .env in project root")
getenv(globals.ENVFILE)
######################################################
##  KUBERNETES SETTINGS
######################################################

KUBECONFIG = "./data/kubeconfig"
KUBECONTEXT = "meeplabben"

################################################################################
##############      The project formerly known as sandboxy     #################
################################################################################
class Project():
    """
    Utilities for managing the repository at a higher level

    - Cleans the temp files
    - cleans docker cluster
    - cleans kubernetes architecture
    - resets to like new state
    - backs up the temp files and persistant data
    """
    def createsandbox(composefile):
        '''
        Creates the sandbox, using kubernetes/docker
        '''
        # set environment to read from kube config directory
        #setenv({"KUBECONFIG":KUBECONFIGPATH})

    def runsandbox(composefile):
        '''
        run a sandbox

        Args:
            composefile (str): composefile to use
        '''
        #import subprocess
        #subprocess.Popen(["docker-compose", "up", composefile])

    def clean_persistant_data(self):
        """
        Cleans temoporary files
        """
        for directory in globals.PERSISTANTDATA:
            for file in listdir(directory):
                if exists(Path(abspath(file))):
                    remove(Path(abspath(file)))



class MenuGrouping():
#    DO NOT MOVE THIS FILE
#    This is the main menu of the project, 
    '''    
Welcome to Meep lab! 

This software initiates a sandboxed environment to be used for:

- practicing hacking
- malware analysis
- networking studies
- secdevops studies
- just about anything needing a strongly sandboxed network of arbitrary computer
    entities with the full ecosystem of docker and kubernetes

Meeplabben, meepabben, meepben! (its dutch, plug it into google translate)
    '''
    def __init__(self):
        """
        MenuGrouping.__init__
        """
        # challenge templates
        self.create_sandbox = Project.createsandbox
        self.start_sandbox = Project.runsandbox
        #self.sandbox_utilities = Project.utilities
        self.cli = Ctfcli

def main():
    fire.Fire(MenuGrouping)

if __name__ == "__main__":
    main()
    #fire.Fire(MenuGrouping)

