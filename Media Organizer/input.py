# ASMITHA ALURI
# MEDIA ORGANIZER
# input.py

from pathlib import Path

def get_directory() -> Path: 
    '''Gets path of directory containing only media that the user would like to filter by month and year.'''
    return Path(input('Please enter the pathname of the directory containing all the files of media you would like to organize: '))