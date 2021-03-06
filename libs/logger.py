#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import sys
import datetime

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


class logger:
    def __init__(self, debug=False):
        self.__debug = debug

        project_path = (os.path.dirname(os.path.abspath(sys.argv[0])))
        file_basename = 'bruteforce_'
        date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        if not os.path.isdir(os.path.join(project_path, 'logs')):
            os.makedirs(os.path.join(project_path, 'logs'))

        log_file_name = os.path.join(project_path, 'logs', file_basename + date + '.log')

        self.file = open(log_file_name, 'w')

    def __exit__(self, type, value, traceback):
        self.file.close()

    def success(self, msg, update=False):
        self.file.write(msg + '\n')
        if update:
            print(GREEN + msg + RESET, end='\r')
        else:
            print(GREEN + msg + RESET)

    def info(self, msg, update=False):
        self.file.write(msg + '\n')
        if update:
            print(WHITE + msg + RESET, end='\r')
        else:
            print(WHITE + msg + RESET)

    def warn(self, msg, update=False):
        self.file.write(msg + '\n')
        if update:
            print(YELLOW + msg + RESET, end='\r')
        else:
            print(YELLOW + msg + RESET)

    def error(self, msg, update=False):
        self.file.write(msg + '\n')
        if update:
            print(RED + msg + RESET, end='\r')
        else:
            print(RED + msg + RESET)
