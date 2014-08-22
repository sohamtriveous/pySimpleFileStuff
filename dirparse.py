__author__ = 'sohammondal'

import sys
import os
import re
import shutil
import commands

def find(pat, str):
    '''
    looks for a simple pattern
    :param pat: regex pattern
    :param str: string where to search for
    :return: true/false
    '''
    match = re.search(pat, str)
    if match:
        return True

def path_join(path, filename):
    '''
    Joins a filename to a given path and then returns the absolute path of the same
    :param path: path
    :param filename: filename that needs to be joined to the path
    :return: the absolute path of the file in teh given path
    '''
    path = os.path.join(path, filename)
    return os.path.abspath(path)


def list(path):
    '''
    Finds all the filenames with the __text__ pattern in the given path
    :param path: path to search for the pattern
    :return: a list of the abspaths of filenames with the said pattern
    '''
    filenames = os.listdir(path)
    filenames_absolute = []
    for filename in filenames:
        match = find('__\w+__', filename)
        if match:
            abs_path = path_join(path, filename)
            print 'Found:', abs_path
            filenames_absolute.append(abs_path)
    return filenames_absolute


def copy_files(path, filenames_absolute=[]):
    '''
    Copies the given files to a given path
    :param path: the destination path where we must copy to
    :param filenames_absolute: a list of the absolute paths of files that need to be copied
    :return:
    '''
    for filename_absolute in filenames_absolute:
        shutil.copy(filename_absolute, path)
    print len(filenames_absolute), 'file(s) copied!'
    return


def zip_files(zip_final_dir, zip_file_name, filenames_absolute=[]):
    '''
    Zips a group of files
    :param zip_final_dir: the directory where we want to store the zipped file
    :param zip_file_name: the name of the resultant zip file
    :param filenames_absolute: a list of hte absolute paths of the files that need to be zipped
    :return:
    '''
    zip_final_path = path_join(zip_final_dir, zip_file_name)
    list_str = " ".join(filenames_absolute)
    cmd = 'zip -j ' + zip_final_path + ' ' + list_str
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        print 'Error while zipping file ', sys.stderr
        sys.exit(1)
    else:
        print 'Successfully zipped', '\'' + zip_file_name + '\'', 'with the following files: ', list_str
    return


def validate_args(args=[]):
    '''
    Validates and starts the parsing procedure
    ./dirparse.py . --todir /tmp/mytempdir
    or
    ./dirparse.py . --tozip hello.zip
    :param args: commandline arguments
    :return:
    '''
    if len(args) != 2 and len(args) != 4:
        print 'usage: [--todir dir][--tozip zipfile] dir dir dir'
        return
    filenames_absolute = []
    dir_base = args[1]
    # convert from path to abspath
    dir_base_abs = os.path.abspath(dir_base)
    print 'Searching in directory:', dir_base_abs

    filenames_absolute = list(dir_base_abs)

    if len(args) > 2:
        operation = args[2]
        operation_param = args[3]
        if operation == '--todir':
            operation_path_abs = os.path.abspath(operation_param)
            copy_files(operation_path_abs, filenames_absolute)
        else:
            if operation == '--tozip':
                zip_files(dir_base_abs, operation_param, filenames_absolute)
    return

validate_args(sys.argv)
