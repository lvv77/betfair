"""File containing the utility classes"""
from __future__ import absolute_import, division, print_function
#Filesystem
import os
#Threading
import threading
#Colors
from colorama import init, Fore, Back, Style
init()
#Sounds
import winsound
#Date
import datetime as dt
#Logging
import json
import logging
import logging.config

class DataStorage(object):
    """Calss containing methods for CSV file manipulation"""
    @staticmethod
    def save_data(data, path, name, index_name='index', headers=True, b_append=False):
        """ 
        Saves passed data to CSV file 

        Parameters 
        ---------- 
        data : dataframe 
            Data to be saved 
        path : string 
            Where to save the data 
        name : string 
            Name of the file 
        index_name : string
            Header label for the index column 
        """
        #Check if folder exists 
        if not os.path.exists(path):
            os.makedirs(path)
        elif b_append & os.path.exists(path + name + '.csv'):
            #Append to existing file
            data_org = pd.read_csv(path + name + '.csv', header=0, low_memory=False, index_col=0)
            data = data_org.append(data)
        data.to_csv(path + name + '.csv', index_label=index_name, header=headers)

class Counter(object):
    """Class for inter-thread counting"""
    def __init__(self, start=0):
        """
        Init counter
        
        Parameters
        ==========
        @start : int
            Initial value of the counter
        """
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        """Increase value"""
        self.lock.acquire()
        try:
            self.value = self.value + 1
        finally:
            self.lock.release()
    def decrement(self):
        """Decrease value"""
        self.lock.acquire()
        try:
            self.value = self.value - 1
        finally:
            self.lock.release()

class Logger(object):
    def __init__(self, **kwargs):
        self.setup_logging()
    def setup_logging(self, default_path='./logs/logging.json', default_level=logging.INFO,
                      env_key='LOG_CFG'):
        """Setup logging configuration"""
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)

    """Helper class containing usefull utilities"""
    def info(self, msg="", color="", level=0, file_logger_name='default_file_logger',
             b_separator=False, b_sound=False, b_file=True):
        """
        Prints log message to console

        Params
        ==============
        @msg : string
            Message to be shown
        @level : int
            Indent level
        @b_separator : Boolean
            Show visual separator after the message?
        @color : Fore.color
            Color of the text
        @b_sound : bool
            Play sound after the message?
        """
        #Prepare loggers
        #Fancy console
        fancy_log = logging.getLogger('fancy_console_logger')
        #File
        file_log = logging.getLogger(file_logger_name)
        #Default offset
        offset = ''
        #Print offset depending on the level
        for i in range(0, level):
            offset += '>>'
        #Print message if there is one
        if msg != "":
            fancy_log.info(color  + offset + ' ' + msg + Style.RESET_ALL)
            if b_file:
                file_log.info(offset + ' ' + msg)
        #Print separator if requested
        if b_separator:
            sep = ''
            #Make the separator nicely aligned
            for i in range(0, 25 - level):
                sep += '=='
            fancy_log.info(color + offset + ' ' + sep + Style.RESET_ALL)
            if b_file:
                file_log.info(offset + ' ' + sep)
        #Play sound if requested
        if b_sound:
            winsound.Beep(1000,1000)
    def error(self, msg="", color="", level=0, file_logger_name='default_file_logger',
             b_separator=False, b_sound=False, b_file=True):
        """
        Prints log message to console

        Params
        ==============
        @msg : string
            Message to be shown
        @level : int
            Indent level
        @b_separator : Boolean
            Show visual separator after the message?
        @color : Fore.color
            Color of the text
        @b_sound : bool
            Play sound after the message?
        """
        #Prepare loggers
        #Fancy console
        fancy_log = logging.getLogger('fancy_console_logger')
        #File
        file_log = logging.getLogger(file_logger_name)
        #Default offset
        offset = ''
        #Print offset depending on the level
        for i in range(0, level):
            offset += '>>'
        #Print message if there is one
        if msg != "":
            fancy_log.error(color  + offset + ' ' + msg + Style.RESET_ALL)
            if b_file:
                file_log.error(offset + ' ' + msg)
        #Print separator if requested
        if b_separator:
            sep = ''
            #Make the separator nicely aligned
            for i in range(0, 25 - level):
                sep += '=='
            fancy_log.error(color + offset + ' ' + sep + Style.RESET_ALL)
            if b_file:
                file_log.error(offset + ' ' + sep)
        #Play sound if requested
        if b_sound:
            winsound.Beep(1000,1000)
    def debug(self, msg="", color="", level=0, file_logger_name='default_file_logger',
             b_separator=False, b_sound=False, b_file=True):
        """
        Prints log message to console

        Params
        ==============
        @msg : string
            Message to be shown
        @level : int
            Indent level
        @b_separator : Boolean
            Show visual separator after the message?
        @color : Fore.color
            Color of the text
        @b_sound : bool
            Play sound after the message?
        """
        #Prepare loggers
        #Fancy console
        fancy_log = logging.getLogger('fancy_console_logger')
        #File
        file_log = logging.getLogger(file_logger_name)
        #Default offset
        offset = ''
        #Print offset depending on the level
        for i in range(0, level):
            offset += '>>'
        #Print message if there is one
        if msg != "":
            fancy_log.debug(color  + offset + ' ' + msg + Style.RESET_ALL)
            if b_file:
                file_log.debug(offset + ' ' + msg)
        #Print separator if requested
        if b_separator:
            sep = ''
            #Make the separator nicely aligned
            for i in range(0, 25 - level):
                sep += '=='
            fancy_log.debug(color + offset + ' ' + sep + Style.RESET_ALL)
            if b_file:
                file_log.debug(offset + ' ' + sep)
        #Play sound if requested
        if b_sound:
            winsound.Beep(1000,1000)
    def warning(self, msg="", color="", level=0, file_logger_name='default_file_logger',
             b_separator=False, b_sound=False, b_file=True):
        """
        Prints log message to console

        Params
        ==============
        @msg : string
            Message to be shown
        @level : int
            Indent level
        @b_separator : Boolean
            Show visual separator after the message?
        @color : Fore.color
            Color of the text
        @b_sound : bool
            Play sound after the message?
        """
        #Prepare loggers
        #Fancy console logger
        #Supports colors
        fancy_log = logging.getLogger('fancy_console_logger')
        #File logger
        file_log = logging.getLogger(file_logger_name)
        #Default offset
        offset = ''
        #Print offset depending on the level
        for i in range(0, level):
            offset += '>>'
        #Print message if there is one
        if msg != "":
            #Console log
            fancy_log.warning(color  + offset + ' ' + msg + Style.RESET_ALL)
            #Lof to file as well
            if b_file:
                file_log.warning(offset + ' ' + msg)
        #Print separator if requested
        if b_separator:
            sep = ''
            #Make the separator nicely aligned
            for i in range(0, 25 - level):
                sep += '=='
            fancy_log.warning(color + offset + ' ' + sep + Style.RESET_ALL)
            if b_file:
                file_log.warning(offset + ' ' + sep)
        #Play sound if requested
        if b_sound:
            winsound.Beep(1000,1000)
    def critical(self, msg="", color="", level=0, file_logger_name='default_file_logger',
             b_separator=False, b_sound=False, b_file=True):
        """
        Prints log message to console

        Params
        ==============
        @msg : string
            Message to be shown
        @level : int
            Indent level
        @b_separator : Boolean
            Show visual separator after the message?
        @color : Fore.color
            Color of the text
        @b_sound : bool
            Play sound after the message?
        """
        #Prepare loggers
        #Fancy console
        fancy_log = logging.getLogger('fancy_console_logger')
        #File
        file_log = logging.getLogger(file_logger_name)
        #Default offset
        offset = ''
        #Print offset depending on the level
        for i in range(0, level):
            offset += '>>'
        #Print message if there is one
        if msg != "":
            fancy_log.critical(color  + offset + ' ' + msg + Style.RESET_ALL)
            if b_file:
                file_log.critical(offset + ' ' + msg)
        #Print separator if requested
        if b_separator:
            sep = ''
            #Make the separator nicely aligned
            for i in range(0, 25 - level):
                sep += '=='
            fancy_log.critical(color + offset + ' ' + sep + Style.RESET_ALL)
            if b_file:
                file_log.critical(offset + ' ' + sep)
        #Play sound if requested
        if b_sound:
            winsound.Beep(1000,1000)