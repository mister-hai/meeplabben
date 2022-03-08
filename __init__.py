# load essentials
from sys import path
from os.path import realpath,abspath

# load utilities
from data.utils import getenv,debugyellow,debuggreen

# import global vars
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

# now we init the globals
globals.paths()

# now load the environment variables into the module
debugyellow("Setting Environment from .env in project root")
getenv(globals.ENVFILE)

# now we load the main module, calling the CTFCLI module
import __main__