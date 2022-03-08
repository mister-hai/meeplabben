from data.utils import debuggreen
from pathlib import Path
import os

def paths():
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
