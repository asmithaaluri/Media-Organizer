# ASMITHA ALURI
# MEDIA ORGANIZER
# main.py

import input
import media_organize

def run():
    directory = input.get_directory()
    organize = media_organize.MediaOrganizer()
    
    try:
        organize.get_all_files_in_directory(directory)
        organize.get_date_of_each_file()
        organize.parse_media_and_date()
    except media_organize.FileError as e:
        print(e)
        return

    print('Process is finished!')


if __name__ == '__main__':
    run()