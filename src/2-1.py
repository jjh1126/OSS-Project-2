# 2-1)

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

# 2-1-1)

print('='*50)
print("2-1-1)")

for year in range(2015, 2019):
  print("[ "+ str(year) +" ]")
  col = ['H','avg','HR','OBP']
  sub_data = data.loc[data['year'] == year , ['batter_name', 'H','avg','HR','OBP']]

  output_dataframe = pd.DataFrame(np.zeros((4, 10)),
                                  index = col,
                                  columns = pd.Index(range(1,11)))
  for c in col:
    series = sub_data[['batter_name', c]].sort_values(by=c, ascending=False).head(10).batter_name
    output_dataframe.loc[c] = series.values

  print(output_dataframe)
  print()


# 2-1-2)

print('\n'+'='*50)
print("2-1-2)")

cp = data['cp'].unique()
tmp = data.loc[data.year==2018]

output_series = pd.Series(np.zeros(cp.size),index=cp)

for c in cp:
  name = tmp.loc[data.cp==c, ['batter_name', 'cp','war']].sort_values(by='war', ascending=False).head(1).batter_name
  output_series[c] = name.values

print(output_series)

# 2-1-3)

print('\n'+'='*50)
print("2-1-3)")

table = data[['salary', 'R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']].corr()
c = table['salary'].abs()

result = c.sort_values(ascending=False).index[1]

print("\'salary\'와 상관관계가 가장 높은 변수는 \'" + result + "\' 입니다.")