"""
Created on Tue Nov 22 15:35:00 2022

@author: Diana Valladares
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import math

## Hypothesis Testing for Responders and Non-Responders

### Ho : Both, responders and non-responders tend to have the same age
### Hi: Reponders and non-responders tend to not have the same age

dfData = pd.read_csv("./data.csv")


#target = 1 respondents 
# target = 0 non-respondednts
print("here")

