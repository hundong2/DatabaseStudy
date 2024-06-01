# import the Fraudit libraries
from fraudit import *

# import commonly-needed built-in libraries
import string, sys, re, random, os, os.path
# import data handling libraries
import pandas as pd
import numpy as np

print("test")
Bid = load("D:/workspace/DatabaseStudy/fraudit/samples/Bid.tbl")
Blacklist = load("D:/workspace/DatabaseStudy/fraudit/samples/Blacklist.tbl")

