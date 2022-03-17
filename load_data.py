from chunk import Chunk
from operator import delitem
import re
import pandas as pd

### Loading Data into Pandas ###

#Loading file CSV
df = pd.read_csv('pokemon_data.csv')
print(df)   #Get all Data
print(df.head(3))   #Get first 3 lines
print(df.tail(3))   #Get the last 3 lines

#Loading file Xlsx
df_xlsx = pd.read_excel('pokemon_data.xlsx')
print(df_xlsx)
print(df_xlsx.head(3))   #Get first 3 lines
print(df_xlsx.tail(3))   #Get the last 3 lines

#Loading file txt
df_txt = pd.read_csv('pokemon_data.txt', delimiter = '\t')
print(df_txt)
print(df_txt.head(3))   #Get first 3 lines
print(df_txt.tail(3))   #Get the last 3 lines

### Reading Data in Pandas ###
#Read heards
print(df.columns)

#Read each Column
print(df['Name'])   #Get all Name
print(df['Name'][0:6])  #Get Name first 6 lines
print(df[['Name', 'Attack', 'HP']])     #Get field

#Read each Row
print(df.head(4))   #Get 4 row

for index,row in df.iterrows():
    print(index, row)   #Get all row

for index,row in df.iterrows():
    print(index, row['Name'])   #Get all row field Name

### Sorting/Describing Data ###

print(df.describe())    #Describing Data

print(df.sort_values('Name'))   #Sort field Name => a b c d ...

print(df.sort_values(['Name', 'HP']))   #Sort field Name, HP Ascending

print(df.sort_values('Name', ascending=False))   #reverse field Name 

# ### Making changes to the Data ###
df['total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']
print(df.head(5))   #add new total column

#drop column 
df= df.drop(columns=['total'])  #Delete colums total

### Saving our Data(Exporting into desired format) ###

df.to_csv('newFile.csv')    #Saving new file csv
df_newFile = pd.read_csv('newFile.csv')
print(df_newFile.head(5))   #add new total column

df.to_csv('newFile.xlsx')    #Saving new file xlsx

df.to_csv('newFile.txt', sep='\t')    #Saving new file txt


### Filtering Data ###
print(df.loc[df['Type 1'] == 'Grass'])  #filtering type 1 = Grass

print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])    #filtering type 1 == Grass and type == Poison and HP > 70

print(df.loc[df['Name'].str.contains('Mega')])  #Filtering field Name with 'Mega' word

print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])     #Filtering firld Name have first word 'pi' +...

### Conditional changes ###
a = df.loc[df['HP'] > 10, ['Generation']] = ['test']
print(a)

### Aggregate statistics(Groupby) ###
print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))    #

print(df.groupby(['Type 1']).sum())     #

print(df.groupby(['Type 1']).count())  

### Working with large amounts of Data ###
for df in pd.read_csv('newFile.csv',chunksize=3):  
    print('Chunk df')
    print(df)

### Create DataFrame ###
peoples = {'name': ['Nguyễn Văn Hiếu', 'Hiếu Nguyễn Văn'], 'age': [28, 28], 'website': ['https://nguyenvanhieu.vn', None]}
df = pd.DataFrame(peoples)
print(df)

# txts = ['chỗ này ăn cũng khá ngon', 'ngon, nhất định sẽ quay lại', 'thái độ phục vụ quá tệ']
labels = [1, 1, 0]
df = pd.DataFrame()
df['txt'] = txts
df['label'] = labels
print(df)

### Connect Dataframe ###
df1 = pd.DataFrame({'name': ['Hiếu'], 'age': [18], 'gender': ['male']})
df2 = pd.DataFrame({'name': ['Nam', 'Mai', 'Hoa'], 'age': [15,17,19]})
df = df1.append(df2, sort=True)
print(df)