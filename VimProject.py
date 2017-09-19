#! /usr/bin/python3

import argparse
import os
import sys
from shutil import copy2

from log import base_logger

# GLOBALS
SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0]

HOME_PATH = os.path.expanduser('~')

RC_PATH = ".vimtemplates"
ARGPARSE_DESCRIPTION = """Copies predefined .vimrc files to the specified path.

The software will first look for a folder named '.vimtemplates' in the user's
home directory and gather any file types (if any), then will search the script
directory for defaults. The software will always prefer files from the home
directory over the script directory.

The files contained in the '.vimtemplates' directories must all be Vim script
files that are to be treated as .vimrc files. Each file name represents the
style of project that it is meant for where a file named 'python3' would have
python3 specific vim settings.
"""


def list_types():
    types = {
        'home': None,
        'script': None,
    }

    if os.access(os.path.join(HOME_PATH, RC_PATH), os.F_OK):
        types['home'] = os.listdir(os.path.join(HOME_PATH, RC_PATH))
        base_logger.debug('home: %s', types['home'])

    if os.access(os.path.join(SCRIPT_PATH, RC_PATH), os.F_OK):
        types['script'] = os.listdir(os.path.join(SCRIPT_PATH, RC_PATH))
        base_logger.debug('script: %s', types['script'])

    return types


def run(pt, path=None):
    """ Copies a .vimrc file from '/vimrc' to the destination.

    Uses the name of the project_type to select files. Therefore, if the user
    specifies "python" at the command line the software will check for a file
    named "python" to copy to the destination directory.

    All files that are copied from the '/vimrc' directory will be renamed to
    '.vimrc' automatically.
    """
    if path is None:
        path = ''

    types_list = list_types()
    if types_list['home'] is not None and types_list['home'].count(pt):
        try:
            copy2(os.path.join(HOME_PATH, RC_PATH, pt),
                  os.path.join(path, '.vimrc'))
        except Exception as e:
            base_logger.critical(str(e))
            raise

        base_logger.info('Copied %s to %s'
                         % (os.path.join(HOME_PATH, RC_PATH, pt),
                            os.path.join(path, '.vimrc')))

    elif types_list['script'] is not None and types_list['script'].count(pt):
        try:
            copy2(os.path.join(SCRIPT_PATH, RC_PATH, pt),
                  os.path.join(path, '.vimrc'))
        except Exception as e:
            base_logger.critical(str(e))
            raise

        base_logger.info('Copied %s to %s'
                         % (os.path.join(SCRIPT_PATH, RC_PATH, pt),
                            os.path.join(path, '.vimrc')))
    else:
        base_logger.warning('Could not find \'%s\'' % pt)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].count('--types'):
        base_logger.disabled = True
        types_list = list_types()
        print('Files found in home directory (%s):\n    %s'
              % (HOME_PATH, types_list['home']))
        print('Files found in script directory (%s):\n    %s'
              % (SCRIPT_PATH, types_list['script']))
        base_logger.disabled = False
        exit()

    parser = argparse.ArgumentParser(description=ARGPARSE_DESCRIPTION)

    parser.add_argument("project_type", help="The type of project to generate "
                        "a .vimrc file for.", type=str)

    parser.add_argument("-p", "--path", help="The path to output the vimrc to. "
                        "Defaults to the current directory", type=str)

    parser.add_argument("--types", help="Simply list the available vimrc "
                        "types.", action="store_true")

    parsed = parser.parse_args()

    run(parsed.project_type, parsed.path)
