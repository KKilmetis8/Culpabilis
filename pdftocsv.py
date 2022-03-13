# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:14:46 2022

@author: Konstantinos
"""

import pandas as pd
import tabula as tb
import glob
import matplotlib.pyplot as plt
import numpy as np
import camelot as cml

#%% Colour Array

# I am peculiar abour colours. I like them like this.
colarr = ['royalblue', 'darkgreen', 'firebrick', 'darkgoldenrod',
          'darkslateblue', 'mediumslateblue']

#%% Data input
# A list of dataframes, one for each page
df_list = tb.read_pdf('pdfs/2020_5.pdf',
                 pages='all',
                 encoding='utf8',
                 stream = True,
                 pandas_options = {'header':None})

# Make one big dataframe
df = pd.concat(df_list)

# The index is fucky because of the concatenation,
# This fixes that
df.reset_index(drop=True, inplace=True)

# Proper, ASCII col names should be the column names
df.columns = ['num','AM','grade']
df.drop([0,0], inplace=True)

# Make it int 
df = df.astype({'grade': int})

#%% Plotting
fig, axs = plt.subplots(1,2)
fig.suptitle(' Tabula vs Camelot in HM:2021-3', fontsize=20)
bin_num = np.arange(0,10 + 1.5 ) - 0.5
axs[0].hist(df['grade'], bins=bin_num, color=colarr[0])
axs[0].set_xticks(np.arange(0, 11, 1))
axs[0].set_title('Tabula', fontsize=15)

#%% With Camelot

tables = cml.read_pdf('pdfs/2020_5.pdf',
                      pages='all')

df_cml = tables[0].df
df_cml.columns = ['num','AM','grade']
df_cml.sort_values(by='grade', axis=0, inplace=True)

bin_num = np.arange(0,10 + 1.5 ) - 0.5
axs[1].hist(df['grade'], bins=bin_num, color=colarr[1])
axs[1].set_xticks(np.arange(0, 11, 1))
axs[1].set_title('Camelot', fontsize=15)
