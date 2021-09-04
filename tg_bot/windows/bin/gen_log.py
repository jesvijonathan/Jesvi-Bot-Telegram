from os import path as op
from sys import path as pat

pa = op.abspath(op.join(op.dirname(__file__), '..', '..'))
pa = pa + "/common"
pat.insert(1, pa)

import general_log_switch

# I suck at file navigation especially in c++, slows me down to a great extent,  thats why using this script as an redirector to general_log_from above