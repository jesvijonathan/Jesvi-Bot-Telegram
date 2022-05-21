from ast import parse
from os import link
from mysql.connector import connection
from telegram.parsemode import ParseMode
import modules.core.extract as extract
import time
import threading
import itertools
from multiprocessing.pool import ThreadPool

import modules.core.database as database

from modules.core.warn import warn

import json

try:
    from config1 import *
except:
    from config import *

# Changelog for next beta-3 update
# get group settings - 
# welcome settings, welcome text, verification type, leave text, leave ban, clear in/out status update, rules display
# rules settings, rules text, priv/public display type
# notes settings, number of active notes, disabled notes,
# filter settings, filter admin, active filter ,disabled filter
# warn settings, number of warnings in group, bumber of warn actions taken, number of blacklist
# help settings, help text
# bio settings, no. of bios,  
# commands, number of disabled commands, 

