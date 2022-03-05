#This file is going to be the main file after start.sh I guess?

# HUGE TODO: SET PATHS CORRECTLY EVERYTHING IS BROKENNNN!!!!!
# repository managment
from ctfcli.__main__ import Ctfcli
from ctfcli.utils.utils import greenprint,errorlogger

from data.dockerpulls import *
from data.utils import putenv,setenv
# basic imports
import subprocess,os,sys,fire
from pathlib import Path
################################################################################
##############                   Master Values                 #################
################################################################################

sys.path.insert(0, os.path.abspath('.'))

#Before we load the menu, we need to do some checks
# The .env needs to be reloaded in the case of other alterations
#
# Where the terminal is located when you run the file
PWD = os.path.realpath(".")
#PWD_LIST = os.listdir(PWD)

# ohh look a global list
global PROJECT_ROOT
PROJECT_ROOT = Path(os.path.dirname(__file__))
global CHALLENGEREPOROOT
CHALLENGEREPOROOT=Path(PROJECT_ROOT,'/data/CTFd')
global COMPOSEDIRECTORY
COMPOSEDIRECTORY = Path(PROJECT_ROOT,'/data/composefiles')
global KUBECONFIGPATH
KUBECONFIGPATH = Path(PROJECT_ROOT, '/data/kubeconfig/')

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
    setenv({"KUBECONFIG":KUBECONFIGPATH})

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
        DO NOT MOVE THIS FILE
    This is the main menu of the project, Project.__init__ is where you
    explicitly define the paths of the folders expected
    This class is where you build the menu calling other actions

    '''
    def __init__(self):
        # challenge templates
        self.name = "lol"
        self.project_actions = Project(PROJECT_ROOT)
        self.cli = Ctfcli()

def main():
   fire.Fire(MenuGrouping)


if __name__ == "__main__":
    main()
    #fire.Fire(Ctfcli)

