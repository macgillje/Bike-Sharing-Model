
# coding: utf-8

# In[76]:

import pandas as pd
import csv as csv
import numpy as np
import math as math


# In[77]:

df_train = pd.read_csv('../Data/train.csv', header=0)

seasons = 4


# In[78]:

survival_table = np.zeros([1, seasons], float)

for i in xrange(seasons):
    biker_rate = sum(df_train.loc[(df_train.season == i+1, 'count')])/len(df_train[(df_train.season == i+1)])
    survival_table[0, i] = biker_rate
    
print survival_table


# In[79]:

test_file = open('../Data/test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()


# In[80]:

predictions_file = open("output_season.csv", "wb")
predictions_file_object = csv.writer(predictions_file)
predictions_file_object.writerow(["datetime", "count"])


# In[81]:

for row in test_file_object:
    predictions_file_object.writerow([row[0], survival_table[0, float(row[1]) - 1]])


# In[ ]:



