import os
import logging
import pathlib
from pathlib import Path

from ctfcli.utils.utils import DEBUG

try:
    #import colorama
    from colorama import init
    init()
    from colorama import Fore, Back, Style
    COLORMEQUALIFIED = True
except ImportError as derp:
    print("[-] NO COLOR PRINTING FUNCTIONS AVAILABLE, Install the Colorama Package from pip")
    COLORMEQUALIFIED = False

################################################################################
##############               LOGGING AND ERRORS                #################
################################################################################
log_file            = 'logfile'
logging.basicConfig(filename=log_file, 
                    #format='%(asctime)s %(message)s', 
                    filemode='w'
                    )
logger              = logging.getLogger()
launchercwd         = pathlib.Path().absolute()

redprint          = lambda text: print(Fore.RED + ' ' +  text + ' ' + Style.RESET_ALL) if (COLORMEQUALIFIED == True) else print(text)
blueprint         = lambda text: print(Fore.BLUE + ' ' +  text + ' ' + Style.RESET_ALL) if (COLORMEQUALIFIED == True) else print(text)
greenprint        = lambda text: print(Fore.GREEN + ' ' +  text + ' ' + Style.RESET_ALL) if (COLORMEQUALIFIED == True) else print(text)
yellowboldprint = lambda text: print(Fore.YELLOW + Style.BRIGHT + ' {} '.format(text) + Style.RESET_ALL) if (COLORMEQUALIFIED == True) else print(text)
makeyellow        = lambda text: Fore.YELLOW + ' ' +  text + ' ' + Style.RESET_ALL if (COLORMEQUALIFIED == True) else None
makered           = lambda text: Fore.RED + ' ' +  text + ' ' + Style.RESET_ALL if (COLORMEQUALIFIED == True) else None
makegreen         = lambda text: Fore.GREEN + ' ' +  text + ' ' + Style.RESET_ALL if (COLORMEQUALIFIED == True) else None
makeblue          = lambda text: Fore.BLUE + ' ' +  text + ' ' + Style.RESET_ALL if (COLORMEQUALIFIED == True) else None
debugred = lambda text: print(Fore.RED + '[DEBUG] ' +  text + ' ' + Style.RESET_ALL) if (DEBUG == True) else None
debugblue = lambda text: print(Fore.BLUE + '[DEBUG] ' +  text + ' ' + Style.RESET_ALL) if (DEBUG == True) else None
debuggreen = lambda text: print(Fore.GREEN + '[DEBUG] ' +  text + ' ' + Style.RESET_ALL) if (DEBUG == True) else None
debugyellow = lambda text: print(Fore.YELLOW + '[DEBUG] ' +  text + ' ' + Style.RESET_ALL) if (DEBUG == True) else None
debuglog     = lambda message: logger.debug(message) 
infolog      = lambda message: logger.info(message)   
warninglog   = lambda message: logger.warning(message) 
errorlog     = lambda message: logger.error(message) 
criticallog  = lambda message: logger.critical(message)

def debug(enable_debug = True):
    """
    Init's debugging utilities and sets global DEBUG
    """
    global DEBUG
    DEBUG = enable_debug

def paths(pwd:Path):
    # ohh look a global list
    global PROJECT_ROOT
    # this is a testing line for small snippets in bpython
    # WHEN THE SHELL IS PWD == PROJECTROOT
    #PROJECT_ROOT = PWD
    #PROJECT_ROOT = Path(os.path.dirname(pwd))
    PROJECT_ROOT = pwd
    # use if in __init__.py
    #PROJECT_ROOT = Path(os.path.dirname(__file__))
    debuggreen(f"Project root located at {PROJECT_ROOT}")

    # The .env needs to be reloaded in the case of other alterations
    global ENVFILE
    ENVFILE = Path(PROJECT_ROOT,'.env')
    debuggreen(f"Env file located at {ENVFILE}")

    # challenges repository
    global CHALLENGEREPOROOT
    CHALLENGEREPOROOT=Path(PROJECT_ROOT) / 'data' / 'CTFd'
    debuggreen(f"Challenge Repository located at {CHALLENGEREPOROOT}")

    # docker-compose files directory
    global COMPOSEDIRECTORY
    COMPOSEDIRECTORY = Path(PROJECT_ROOT)/ "data" / "composefiles"
    debuggreen(f"Docker Compose directory located at {COMPOSEDIRECTORY}")

    # kubernetes configuration directory
    global KUBECONFIGPATH
    KUBECONFIGPATH = Path(PROJECT_ROOT) / 'data' / 'kubeconfig'
    debuggreen(f"kubectl config located at {KUBECONFIGPATH}")
