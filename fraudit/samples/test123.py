# import the Fraudit libraries
from fraudit import *

# import commonly-needed built-in libraries
import string, sys, re, random, os, os.path
# import data handling libraries
import pandas as pd
import numpy as np

리스트 = ['외상매출금', '상품매출금', '제품매출' ]

for i in range(len(리스트)):
    if i == 0: 
        a = "계정과목 == '{}'".format(리스트[i])
    else :
        a = a + " or 계정과목 == '{}'".format(리스트[i])
        
res1 = Simple.select(분개장예제, a)
res1.view()