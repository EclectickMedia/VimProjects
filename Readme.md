A simple utility to help manage multiple `.vimrc` files.

Allows the user to store multiple separate `.vimrc` files in a single location and provide a simple interface to place different styles of `.vimrc`'s to a project directory.

## Usage
```
usage: VimProject.py [-h] [-p PATH] [--types] project_type

Copies predefined .vimrc files to the specified path. The software will first
look for a folder named '.vimtemplates' in the user's home directory and
gather any file types (if any), then will search the script directory for
defaults. The software will always prefer files from the home directory over
the script directory. The files contained in the '.vimtemplates' directories
must all be Vim script files that are to be treated as .vimrc files. Each file
name represents the style of project that it is meant for where a file named
'python3' would have python3 specific vim settings.

positional arguments:
  project_type          The type of project to generate a .vimrc file for.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  The path to output the vimrc to.
  --types               Simply list the available vimrc types.
```
