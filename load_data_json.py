import pandas as pd

df_json = pd.read_json('data.json')
# print(df_json.head())

#Read each Column
print(df_json['name'])   #Get all Name

print(df_json.describe())     #Describing Data

new_df = df_json.sort_values(['name', 'age'])  #Sort field name and age

new_df.to_json('newFile.json')   #Saving new file json

print(df_json.loc[df_json['name'] == 'Huy'])  #filtering name = Huy
