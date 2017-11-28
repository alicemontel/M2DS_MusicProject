import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
matplotlib.rcParams.update({'font.size': 16})

data = pd.read_csv('../Source/responses.csv')
pd.set_option('display.max_columns',152)
pd.set_option('display.max_rows',500)
data.head(2)
#print data

#print data.shape
#(1010,150)

#print data.describe()

def display_mat_music():
    music = data.iloc[0:,1:19].copy()

    fig = plt.figure(figsize=(18,18))
    ax = fig.add_subplot(111)
    cax = ax.matshow(music.corr())
    fig.colorbar(cax)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.set_xticklabels([' ']+music.columns.tolist()  ,rotation=90 )
    ax.set_yticklabels([' ']+music.columns.tolist()   )

    plt.show()

# gives the numever of missing values for each attributes
def count_null_data():
    values = data.isnull().sum()
    print values

# delete the columns in which there are >10 missing values
def clean_data():
    list_delete=[]
    values = data.isnull().sum()
    for i in range(len(values)) :
        if values[i]>10 :
            print values[i]
            list_delete.append(i)
    data.drop(data.columns[list_delete],axis=1,inplace=True)
    print data.shape

# delete the rows if music columns are empty
def clean_music_data():
    list_delete=[]
    values =  data.iloc[0:,2:19].copy().isnull().sum()
    for i in range(len(values)) :
        if values[i]>10 :
            print values[i]
            list_delete.append(i)
    data.drop(data.columns[list_delete],axis=1,inplace=True)
    print data.shape

def normal_nan_data():
    list_split = []
    normal_data = pd.get_dummies(data)
    return normal_data
    #normal_data = pnd.get_dummies(data,prefix=list_split)
    #print normal_data.shape


clean_music_data()
normal_nan_data()
