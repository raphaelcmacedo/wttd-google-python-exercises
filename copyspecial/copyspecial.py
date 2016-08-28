#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import zipfile


def get_special_paths(dir):
    absolute_paths = []
    files = os.listdir(dir)

    for file_name in files:
        match = re.search(r'__(\w+)__', file_name)
        if match:
            absolute_paths.append(os.path.abspath(os.path.join(dir, file_name)))

    return absolute_paths


def copy_to(paths, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

    for path in paths:
        file_name = os.path.basename(path)
        new_path = os.path.join(dir, file_name)

        if os.path.exists(new_path):
            os.remove(new_path)
        shutil.copy(path, new_path)


def zip_to(paths, zip_dir):
    with zipfile.ZipFile(zip_dir, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in paths:
            zf.write(path, os.path.basename(path))


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    paths = []
    for dir in args:
        paths.extend(get_special_paths(dir))

    # I'm always printing the paths and running the 2 methods (when set) for teaching purposes
    print('Special paths:')
    print('\n'.join(paths))

    if todir:
        copy_to(paths, todir)
    if tozip:
        zip_to(paths, tozip)


if __name__ == "__main__":
    main()
