import numpy as np
import pandas as pd
import sys
import re
from collections import Counter

from bs4 import BeautifulSoup
import requests

import matplotlib.pyplot as plt

import plotly.plotly as py1
import plotly.offline as py
py.init_notebook_mode(connected=True)

from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)

import plotly.graph_objs as go
import plotly.offline as offline
offline.init_notebook_mode()

from plotly import tools

import warnings
warnings.filterwarnings('ignore')

import sklearn