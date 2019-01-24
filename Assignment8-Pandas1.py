#1) How-to-count-distance-to-the-previous-zero
#For each value, count the difference of the distance from the previous zero 
#(or the start of the Series, whichever is closer) and if there are no 
#previous zeros,print the position Consider a DataFrame df where there is an 
#integer column {'X':[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]}
#The values should therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2].
#Make this a new column 'Y'.
#import pandas as pd
#df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

import numpy as np 
import pandas as pd

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
df
def distance(x):
    y=0
    j = []
    for i in x: 
        if i == 0:
            y = 0
            j.append(y)
        else: 
            y = y+1 
            j.append(y)
    return j 
df['Y'] = df.loc[:,['X']].apply(distance)
print ('Distance to the previous zero is as under: \n', df)

#2) Create a DatetimeIndex that contains each business day of 2015 
#and use it to index a Series of random numbers.
ind = pd.date_range(start = '01-Jan-2015', end = '31-Dec-2015', freq = 'B')
dat = np.random.randn(261)
col = 'Random'
kf = pd.DataFrame (index = ind, data = dat)
kf['Random'] = kf[0]
del kf [0]
print ('DatetimeIndex with series of random numbers: \n', kf.head() )

#3) Find the sum of the values in s for every Wednesday
kf ['Day'] = kf.index.weekday
kf.head(20)
kw = kf[kf['Day'] == 2]
total = kw['Random'].sum()
print ('The sum of values for every Wednesday \n', total)

#4) Average For each calendar month
kw.head(20)
type(kf)
km = kf['Random'].resample ('M').mean()
print('The Average for each calendar month: \n', km) 

#5) For each group of four consecutive calendar months in s, 
#find the date on which the highest value occurred.
kq = kf['Random'].resample ('4MS').max()
kq.head()
kr = kf.loc[kf['Random']==kq[2]]
print ('The date on which the highest value occured is: \n', kr)

















        
