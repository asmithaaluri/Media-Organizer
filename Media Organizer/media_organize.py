# ASMITHA ALURI
# MEDIA ORGANIZER
# media_organize.py

from pathlib import Path
import datetime

MONTH_DICT = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'Ocotober', 11: 'November', 12: 'December'}

class FileError(Exception):
    def __str__(self):
        return "ERROR: Not a valid Path."

class MediaOrganizer:
    def __init__(self):
        self._all_files = []
        self._media_and_date = dict()  

    def get_all_files_in_directory(self, directory: Path) -> None:
        '''Adds the pathnames of the files in the directory to a list. Uses recursion for subdirectories. Skips over directory names that start with a month by assuming that that directory was created by this program.'''
        try:
            for file in directory.iterdir():
                if file.is_file():
                    self._all_files.append(file)
                elif file.is_dir():
                    starts_with_month = (file.name.startswith(month) for month in MONTH_DICT.values())
                    if starts_with_month:
                        continue
                    else:
                        self.get_all_files_in_directory(file)
        except:
            raise FileError
    
    def get_date_of_each_file(self) -> None:
        '''Uses last modified date of each file in the list to determine the date when the media was created (i.e. the date when picture or video was made). A dictionary is populated where the key is the media file and the value is the date of the file.'''
        for file in self._all_files:
            timestamp = file.stat().st_mtime
            date = datetime.date.fromtimestamp(timestamp)
            self._media_and_date[file] = date

    def parse_media_and_date(self) -> None:
        '''Looks through the dictionary to see if a directory that has a media file's month and year as its title exists. If it does not exist, a new directory is made. Then, the media file is moved to the new directory. If a directory that has a media file's month and year as its title already exists, the media file is moved to that directory.'''
        for media_file, date in self._media_and_date.items():
            month = self.get_file_month(date)
            year = self.get_file_year(date)
            new_directory = Path(f'{media_file.parent}/{month} {year}')
            if not Path(new_directory).is_dir():
                new_directory.mkdir(parents=True, exist_ok=True)
            self.move_file(media_file, new_directory)

    @staticmethod
    def get_file_month(date: datetime) -> str:
        '''Dictionary used to specify what number connects to which month. The month of the datetime object is returned.'''
        return MONTH_DICT[date.month]

    @staticmethod
    def get_file_year(date: datetime) -> str:
        '''Year of the datetime object is returned.'''
        return date.year

    @staticmethod
    def move_file(media_file: Path, new_directory: Path) -> None:
        '''File is moved to its designated directory titled by the month and year.'''
        old_media_file = media_file
        new_media_file = Path(f'{new_directory}/{media_file.name}')
        old_media_file.rename(new_media_file)