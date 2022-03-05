import os,sys,subprocess
from ctfcli.utils.utils import greenprint,errorlogger
from pygments import formatters, highlight, lexers
from pygments.util import ClassNotFound
from simple_term_menu import TerminalMenu


###############################################################################
##                          envsubst clone
###############################################################################
def putenv(key,value):
    """
    Puts an environment variable in place

    For working in the interactive mode when run with
    >>> hacklab.py -- --interactive
    """
    try:
        os.environ[key] = value
        greenprint(f"[+] {key} Env variable set to {value}")
    except Exception:
        errorlogger(f"[-] Failed to set {key} with {value}")

def setenv(**kwargs):
    '''
    sets the environment variables given by **kwargs

    The double asterisk form of **kwargs is used to pass a keyworded,
    variable-length argument dictionary to a function.
    '''
    try:
        if __name__ !="" and len(kwargs) > 0:
            projectname = __name__
            for key,value in kwargs:
                putenv(key,value)

            putenv("COMPOSE_PROJECT_NAME", projectname)
        else:
            raise Exception
    except Exception:
        errorlogger("""[-] Failed to set environment variables!\n
    this is an extremely important step and the program must exit now. \n
    A log has been created with the information from the error shown,  \n
    please provide this information to the github issue tracker""")
        sys.exit(1)


def certbot(siteurl):
    '''
    creates cert with certbot
    '''
    generatecert = 'certbot --standalone -d {}'.format(siteurl)
    subprocess.call(generatecert)

def certbotrenew():
    renewcert = '''certbot renew --pre-hook "docker-compose -f path/to/docker-compose.yml down" --post-hook "docker-compose -f path/to/docker-compose.yml up -d"'''
    subprocess.call(certbotrenew)

#lol so I know to implement it later
#certbot(siteurl)

def highlight_file(filepath):
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath,
                                              stripnl=False,
                                              stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def list_files(directory="."):
    return (file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file)))


def main():
    terminal_menu = TerminalMenu(list_files(), preview_command=highlight_file, preview_size=0.75)
    menu_entry_index = terminal_menu.show()
