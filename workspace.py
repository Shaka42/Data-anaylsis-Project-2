import pandas as pd
import numpy as np

df = pd.read_csv('adult.data.csv',sep=',')
# print('Bachelors_degree',round((df[df['education']=='Bachelor'].sum())/(df.sum()),1)*100)
df[df.salary.isin(['>50K'])&(df['native-country'].isin(['India']))][['occupation','native-country','salary']].occupation.value_counts().idxmax()